# 能力矩阵：配置到哪一步，能做什么

这份表回答三个问题：**只装包能干什么、补哪些依赖能到哪一步、哪些必须自备软件/授权**。  
证据等级：**[已跑通]** 在作者机器上用真实或合成边界数据跑过；**[组件可用]** 入口/脚本在，风格检查通过，未用你的数据验收；**[需外部]** 需要自备软件；**[未纳入]** 本版不含。

## 第一层：只装包 + Python 3.11+

| 能力 | 状态 | 说明 |
|---|---|---|
| 六个技能被发现与加载 | [已跑通] | `install.py --smoke`、`examples/quickstart_smoke.py` 验证 |
| 默认路由（说任务进对应核心） | [已跑通] | 写入 `AGENTS.md` 受管块，doctor 确认只出现一次 |
| 安装/升级/回滚/自检 | [已跑通] | `install.py`、`tools/doctor.py`、`tools/manifest.py` |
| 模块检索与可选模块定位 | [已跑通] | `tools/workbench.py search [--optional]` |
| 逐文件用途索引 | [已跑通] | `docs/INVENTORY.md` / `inventory.csv` / `inventory.html` |
| 读取方法/流程/边界文档 | [已跑通] | 全部 `references/` 与 `WORKFLOW.md` 是纯文本 |

这一层不需要任何专业软件，但**不能**做实际计算、读原始谱或处理 CIF。

## 第二层：+ `foundation`（rdkit、Pillow）

| 能力 | 状态 | 入口 |
|---|---|---|
| SMILES/MOL/SDF 规范化、格式转换 | [已跑通] | `organic-chemistry-reasoning/scripts/structure_cli.py` |
| 结构绘制（PNG/SVG） | [已跑通] | 同上 |
| 分子式、精确质量、基本描述符 | [已跑通] | 同上 / `rdkit` 模块脚本 |
| 离线图片识图（OCSR） | [组件可用] | 需 `--profile ocsr`（MolVec jar + Java） |

不包含：反应预测、逆合成、机理自动推断（这些是方法/推理，不是脚本一键）。

## 第三层：+ `spectra` / `thermo-raw`

| 能力 | 状态 | 入口 | 备注 |
|---|---|---|---|
| 读 Bruker 一维/二维（fid/ser + pdata） | [已跑通] | `read_spectral_file.py` | 真实 65536 点 1D、512×4096 2D 处理谱 |
| 读 Varian / NMRPipe | [已跑通] | 同上 | 合成边界文件 |
| 读 mzML / mzXML / MGF / JCAMP / CSV | [已跑通] | 同上 | pyOpenMS + 自带解析 |
| 读 Thermo `.raw` | [需外部] | 同上 | 需 ThermoRawFileParser（`--profile thermo-raw` 可装） |
| 1D 处理、峰表、积分 | [组件可用] | `process_1d.py`、`evidence_cli.py` | 不做自动结构归属 |
| 多谱数值证据（位移/J 统计） | [组件可用] | `evidence_cli.py selftest` | 输出证据，不给结论 |
| 谱图绘图 | [已跑通] | matplotlib | — |

不包含：相位/基线/NUS 重建、定量方法验证、自动结构确证。

## 第四层：+ `crystal`（gemmi 等）

| 能力 | 状态 | 入口 |
|---|---|---|
| 读 CIF/HKL、合并元数据 | [组件可用] | `scxrd-refinement/scripts/08_cif.py` |
| 输入盘点、配体准备、包审计 | [已跑通] | `inventory_crystal_input.py`、`prepare_ligand.py`、`validate_crystal_package.py` |
| checkCIF 提交与报告整理 | [组件可用] | `09_checkcif.py`（需网络） |
| 交付打包（哈希/清单） | [已跑通] | `10_delivery.py` |

不包含：衍射帧还原、解结构、精修、孪晶处理——这些要 DIALS + SHELXT/SHELXL + Olex2。

## 第五层：+ 专业软件（自备/授权）

| 能力 | 需要 | 状态 |
|---|---|---|
| 原始帧 → 指标化/积分/标度 → HKL | DIALS | [组件可用] 分阶段脚本在 `scripts/dials_*.py`；本版未重跑全链 |
| 解结构 / 精修 / 孪晶 / 无序 | SHELXT、SHELXL、Olex2、PLATON | [组件可用] 方法参考完整，程序自备 |
| 构象采样（本地） | xTB、GROMACS、Molclus | [已跑通] 正丁烷 1 ps xTB MD；GROMACS AMD HIP 版短程测试 |
| DFT 优化/频率、GIAO/J | Gaussian 或 ORCA | [已跑通] 水分子优化/频率/GIAO 小型测试；脚本 `prepare_nmr_jobs.py`、`run_gaussian_nmr.py` |
| 构象加权、标度（Bally/DU4） | 已有 FC 数据 | [组件可用] `coupling_postprocess.py` |
| 谱图人工复核 | Mnova 等 | [需外部] 包装不含 |

不包含：任意分子“一键跑完”的自动化；方法/基组/溶剂/参照的匹配仍需人工判断。

## 第六层：集群与授权软件

| 能力 | 状态 | 说明 |
|---|---|---|
| 集群任务构建/提交/回收 | [组件可用] | `hpc-*` 模块是方法+清单，不含站点凭据 |
| ADF/AMS 等 SOC 相对论 NMR | [需外部] | 商业授权，不随包 |
| 大规模模型/数据库/GPU 构建 | [未纳入] | 按需自行配置 |

## 能否实现“迁移到别的电脑、得到同样体验”

| 你的目的 | 满足度 | 说明 |
|---|---|---|
| 在别的电脑装上同样的六个技能 | ✅ | `install.py --host dsh/codex/both/auto` + 校验 + 回滚 |
| 用自然语言触发四个化学核心 | ✅ | `AGENTS.md` 受管默认路由 |
| 先跑通基础能力（结构/格式/谱读取） | ✅ | `foundation` + `spectra` 两个 profile 即可 |
| 完整复现作者的全部科研能力 | ⚠️ 部分 | 需要自备同款专业软件与授权；集群/商业软件不在包内 |
| 完整复现作者的本地库内容 | ⚠️ 部分 | 公开版是精简版：单晶上游模块正文用 `fetch-source crystal` 取；32 个写作可选模块用 `restore-optional` 从 v1.1.0 恢复；ARS 评测数据已剔除 |
| 不看文档就能自己配好 | ⚠️ 需读 2 篇 | `QUICKSTART.md` + `TROUBLESHOOTING.md`；`doctor` 会给下一步命令 |

## 一句话结论

- **装完即得**：可发现、可路由、可自检、可回滚的六技能框架 + 基础结构/谱数据能力。
- **配完开源依赖**：结构编辑、NMR/MS 读取、CIF 读取、Word/PPT 成品都能跑。
- **科学计算要自备软件**：单晶还原/精修、DFT/NMR、MD 采样需要 DIALS/SHELX/Gaussian/ORCA/xTB/GROMACS；包装提供方法、脚本、模板和排错经验，不提供程序和授权。
- **迁移目的可以达成**，但“完整复现作者机器”需要你补同样的后端；`docs/WORKFLOWS.md` 的软件矩阵就是补件清单。