# 化学科研技能：四核心，双学术支持

四个分别完整的化学核心是主要工作入口，两个学术技能为它们提供文献证据与表达支持。换一台电脑也能得到同样体验：安装 → 自检 → 直接说任务。

```bash
python install.py --check          # 只校验，不写文件
python install.py --host dsh       # 或 codex / both / auto
python tools/doctor.py             # 自检并给出下一步命令
```

## 你会得到什么

| 得到 | 说明 |
|---|---|
| 六个技能入口 | 单晶、计算化学、解谱、有机推断、学术检索、学术写作；内部模块不注册为平级技能 |
| 默认路由 | 一段受管规则写进 `AGENTS.md`：说“修单晶 / 算核磁 / 解谱 / 有机 / 找文献 / 写作”进入对应核心 |
| 可发现、可回滚的安装 | 校验 MANIFEST → 复制 → 写安装标记；冲突拒绝覆盖，`--replace` 先备份 |
| 自检与配置工具 | `tools/doctor.py`（只读体检）、`tools/workbench.py`（按 profile 建独立环境） |
| 文档与索引 | 5 分钟上手、真实工作流、逐文件用途索引（Markdown/CSV/可搜索 HTML）、故障处理、维护者手册 |

## 六个技能

| 任务 | 主技能 | 实际内容 |
|---|---|---|
| 衍射数据、单晶解结构与精修 | `scxrd-refinement` | DIALS 还原 → SHELXT/SHELXL/Olex2；孪晶、无序、checkCIF、CIF/FCF 交付 |
| 构象搜索与核磁计算 | `huangjt-computational-chemistry` | xTB/GROMACS 采样 → DFT 优化/频率 → GIAO/J → 标度与加权 |
| 真实核磁/质谱与结构鉴定 | `huangjt-spectral-structure-analysis` | Bruker/Varian/NMRPipe、Thermo RAW/mzML/MGF 读取，多谱归属与候选对照 |
| 有机反应、结构与机理 | `organic-chemistry-reasoning` | 结构身份/绘制/转换、机理与重排、选择性、实验复盘、跨核心组织证据 |
| 文献与先例检索 | `huangjt-academic-research` | 条件、SI、DOI、引文核验、Zotero；系统综述按需启用 ARS |
| 论文与汇报成品 | `huangjt-academic-writing` | 论文/润色/审稿回复/开题学位/Word-PPT，七个默认模块 |

## 配置基础能力，再按需补专业软件

```bash
python tools/workbench.py setup --profile foundation --apply   # 结构识别/绘制/转换
python tools/workbench.py setup --profile spectra --apply      # NMR/MS 读取与绘图
python tools/workbench.py setup --profile thermo-raw --apply   # Thermo RAW 转换
```

`--apply` 在数据目录建独立环境，不改你现有的 Python。Gaussian、ORCA、DIALS、SHELX、GROMACS、Mnova 等使用目标机已有的合法软件；集群是可选项。分享的是方法、脚本、模板与配置工具，**不捆绑程序、账号或样品**。

## 文档

- [5 分钟上手](docs/QUICKSTART.md) · [故障处理](docs/TROUBLESHOOTING.md)
- [真实工作流与软件依赖](docs/WORKFLOWS.md) · [四核心方法与脚本总目录](docs/CATALOG.md)
- [逐文件用途索引](docs/INVENTORY.md)（或打开 [inventory.html](docs/inventory.html) 搜索）
- [基础功能与边界](docs/CORE_ACCEPTANCE.md) · [迁移](docs/MIGRATION.md) · [维护者手册](docs/MAINTAINERS.md)

## 学术支持保持收敛

学术研究负责找文献、SI、条件、先例和引文核验。学术写作默认从 39 项收敛到 7 项：论文、润色、审稿回复、开题、学位论文、Word/PPT 和共享资源。32 项统计/机器学习/海报/专利及重复成品管线退出默认安装包，知识索引和原件恢复见 [可选方法](skills/huangjt-academic-writing/references/optional-methods.md)；它们保留在本地与 v1.1.0 固定版本，按需恢复，不重新注册平级技能。

## 交付状态与边界

安装完成只代表文件完整、入口可发现，不代表任意输入都能一键得到科学结论。各核心已验证/未验证的范围见 [CORE_ACCEPTANCE.md](docs/CORE_ACCEPTANCE.md)；v1.3.0 恢复了完整 CI（账本、索引、测试、离线冒烟），发布说明见 [docs/RELEASE-v1.3.0.md](docs/RELEASE-v1.3.0.md)。第三方来源与许可保留在各技能及 [THIRD_PARTY.md](THIRD_PARTY.md)。