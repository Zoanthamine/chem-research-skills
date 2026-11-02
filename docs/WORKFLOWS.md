# 真实工作流与软件依赖

这份文档回答“这套技能到底怎么用”：每条工作流从什么输入开始、经过哪些阶段、哪一段需要外部软件、哪些结论有证据、哪些还没有。

标注约定：**[已验证]** = 在作者机器上用真实（或合成边界）数据跑通过；**[组件可用]** = 程序入口存在、风格检查通过，但没有用用户数据完整验收；**[未验证]** = 只有方法描述。边界细节见 [CORE_ACCEPTANCE.md](CORE_ACCEPTANCE.md)。

## 总览

| 工作流 | 入口技能 | 输入 | 关键外部软件 | 交付物 |
|---|---|---|---|---|
| 单晶还原与精修 | `scxrd-refinement` | 衍射帧 / CIF / HKL | DIALS、SHELXL/SHELXT、Olex2、PLATON | 精修模型、CIF/FCF、checkCIF 报告 |
| 构象加权核磁计算 | `huangjt-computational-chemistry` | 结构（PDB/XYZ/SMILES） | xTB、GROMACS、Gaussian/ORCA、Molclus | 构象分布、屏蔽/位移、J 耦合、对比表 |
| 谱图读取与结构鉴定 | `huangjt-spectral-structure-analysis` | Bruker/Varian/NMRPipe、Thermo RAW/mzML/MGF | ThermoRawFileParser、pyOpenMS、（可选）Mnova | 证据目录、峰表、归属候选对照 |
| 有机反应与机理判断 | `organic-chemistry-reasoning` | 结构式、条件、观察结果 | RDKit/Open Babel（随环境）、Ketcher（可选） | 机理/选择性分析、对照实验建议 |
| 文献与先例检索 | `huangjt-academic-research` | 结构/反应/关键词/DOI | 检索服务、Zotero（可选） | 条件表、SI 摘录、引文核验 |
| 论文与汇报成品 | `huangjt-academic-writing` | 分析结果、图表、草稿 | Word/PPT 管线、绘图库 | 论文段落、PPT/Word、审稿回复 |

## 1 单晶：原始帧 → 可交付结构

```text
衍射帧 ──DIALS──▶ 指标化/积分/标度 ──▶ HKL ──SHELXT/SHELXL──▶ 模型
        │                                   │
        └─ 实验几何与来源记录                └─ checkCIF/PLATON ──▶ CIF + FCF + 报告
```

- **输入**：整份帧数据（含几何文件），或别人给的 CIF/HKL/INS。
- **关键判断**：只有 CIF/HKL 时不能“重新积分”；报告里要区分“原始数据还原”与“只做精修”。
- **本库提供**：`scripts/dials_stage.py`（分阶段运行并保留日志）、`01_diagnose` → `03_run` → `04_summarize` 流程、`08_cif`、`09_checkcif`、`10_delivery`、无序/孪晶/氢原子专题参考。**[已验证：DIALS 3.30 分阶段入口；另有一次真实数据经验；本版未重跑全链]**
- **软件**：DIALS 用于还原；SHELX/Olex2 用于解结构与精修；PLATON 辅助检查。三者都需自备并合法授权（SHELX 学术免费但需申请）。
- **交付**：CIF+FCF+checkCIF+哈希清单，见 `references/package-audit.md`。

## 2 计算：采样 → DFT → 核磁

```text
结构 ──xTB/GROMACS──▶ 轨迹帧 ──Molclus/xTB──▶ 去重排序 ──▶ 前 N 个构象
                                                        │
                        Gaussian/ORCA: opt+freq ──▶ GIAO 屏蔽 / J ──▶ 标度与加权
                                                        │
                                              与实验位移/J 对比（DP4+/STS 类方法）
```

- **两条采样路线**：本机 xTB 短程 MD（快、覆盖有限）；GROMACS（新分子要重新参数化，不能复用旧分子拓扑/RESP）。**[已验证：正丁烷 1 ps xTB MD；GROMACS AMD HIP 版入口与短程测试]**
- **输入准备**：`prepare_nmr_jobs.py` 从选中的 XYZ 批量生成 opt/freq、GIAO/J 输入；`run_gaussian_nmr.py` 在本机执行并保留原始屏蔽。**[已验证：水分子优化/频率/GIAO 小型测试]**
- **后处理**：`coupling_postprocess.py` 做 Bally/DU4 基组标度与显式构象加权；化学位移参照与标度必须与计算方法匹配。
- **软件**：xTB、GROMACS、Gaussian 或 ORCA；Molclus 可选（去重排序）；Multiwfn/Shermo 可选（波函数、热化学）。作者机器上 Gaussian 位于 `E:/G16W/g16.exe`，只查 PATH 会漏掉，必须用显式路径或环境变量。
- **边界**：采样、选构象、DFT、NMR、参照标度、加权是六个阶段；“有脚本”不等于“任意分子一键完成”。`run_gaussian_nmr.py` 当前以屏蔽提取为主，FC/J 的完整解析仍需人工判断。

## 3 解谱：真实文件 → 证据化归属

```text
Bruker/Varian/NMRPipe / Thermo RAW / mzML/MGF
        │ read_spectral_file.py（保留元数据与哈希）
        ▼
   证据目录（原始副本 + 解析结果 + 日志）
        │ process_1d / spectrum-analyzer / nmrglue
        ▼
 峰表、积分、二维相关、候选结构对照 ──▶ 归属结论（附证据与反证）
```

- **输入**：整份实验目录或文件；多实验时必须指定，不能静默挑一个。
- **已验证**：真实 Thermo RAW（897 张谱、986220 个峰）、真实 Bruker 一维（65536 点）/二维（512×4096 点）处理谱；Bruker/Varian/NMRPipe/mzML/MGF 合成边界测试。**[已验证]**
- **软件**：Thermo RAW 需要 ThermoRawFileParser；pyOpenMS 解析 mzML；nmrglue 处理 NMR；Mnova 是人工复核的可选 GUI，包装不含。
- **边界**：读取≠重新处理≠定量≠结构归属。相位/基线/NUS 重建、定量积分、NOE 距离换算都要单独给依据。

## 4 有机：反应是否成立、为什么

```text
结构/条件/观察 ──▶ 结构身份（SMILES/立体）──▶ 机理与竞争路径
        │                                   ├─ 选择性（位阻/电子/配位）
        │                                   ├─ 重排与副产物
        │                                   └─ 后处理（淬灭/萃取/分离）
        └─ 需要实测证据时：交解谱；需要能量/构象时：交计算；需要先例时：交检索
```

- **本库提供**：`scripts/structure_cli.py`（规范化、绘制、格式转换、离线识图）、`workbench.py`（依赖配置/模块搜索/来源获取）、机理与选择性参考、实验设计/统计/不确定性模块。
- **规则**：区分“用户观察”“文献事实”“模型推断”；没有依据时给可检验的对照实验，不编造结论。

## 5 学术：检索证据与成品

- **检索**：结构/反应类型/条件 → 先例、SI、DOI、引文核验；查不到全文时明确访问范围，保留未知字段。
- **写作**：论文/润色/审稿回复/开题学位/Word-PPT 七个默认模块；32 个统计/ML/海报/专利模块退出默认包，可按需恢复（`workbench.py search --optional`）。
- **交接**：写作不替代检索；单篇精读交学术研究，数据解释交对应化学核心。

## 软件依赖矩阵

| 阶段 | 必需 | 可选 | 本库是否随包 |
|---|---|---|---|
| 结构识别/绘制/转换 | rdkit + Pillow | Open Babel、Ketcher、MolVec | 脚本随包，程序不随包 |
| NMR/MS 读取 | Python 3.11+ | nmrglue、pyOpenMS、ThermoRawFileParser | 脚本随包，程序不随包 |
| 单晶 | DIALS、SHELX、Olex2 | PLATON、GSAS-II | 否 |
| 量化 | Gaussian 或 ORCA、xTB | GROMACS、Molclus、Multiwfn、Shermo | 否 |
| 成品 | python-docx/python-pptx | LibreOffice（渲染）、绘图库 | 否 |

作者机器的统一入口是 `environments.json` + `science.ps1`（单一事实源）；换机器时**不要复制作者路径**，用 `tools/doctor.py` 看你自己的环境，用 `tools/workbench.py` 配置开源部分。

## 常见误区

- 把 `scripts/` 里所有文件当“科研功能”：其中还有函数库、测试和编码辅助。
- 把样例配置当本机参数：`assets/` 里是样例，不是你的仪器设置。
- 把“程序能启动”当“流程已验证”：入口、版本、许可、方法匹配是四件事。
- 把可选模块当已安装：默认包不含那 32 个模块的正文，恢复后也要重新验证。
- 在 Windows 上只查 PATH：Gaussian、CYLview、Mnova 这类 GUI 安装常不写 PATH。