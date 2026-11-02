# 化学科研技能：四核心，双学术支持

四个分别完整的化学核心是主要工作入口，两个学术技能为它们提供文献证据与表达支持。

| 核心任务 | 主技能与实际入口 |
|---|---|
| 衍射数据、单晶解结构与精修 | scxrd-refinement：DIALS 导入至积分/标度/导出，SHELXT/SHELXL/Olex2，孪晶无序和验证交付 |
| 本地构象搜索与核磁计算 | huangjt-computational-chemistry：xTB/GROMACS 采样，选构象、DFT 优化/频率、GIAO/J、标度与加权 |
| 实际核磁/质谱文件与结构鉴定 | huangjt-spectral-structure-analysis：Bruker/Varian/NMRPipe、Thermo RAW/mzML/MGF，数据处理与多谱判断 |
| 有机反应、结构和机理 | organic-chemistry-reasoning：结构工具、机理/重排、选择性、实验复盘，并组织其他核心的证据 |

[四核心方法与脚本总目录](docs/CATALOG.md) · [具体基础功能](docs/CORE_ACCEPTANCE.md) · [新电脑配置](docs/FIRST_RUN.md) · [迁移步骤](docs/MIGRATION.md)

## 安装

从 [最新版下载页](https://github.com/Zoanthamine/chem-research-skills/releases/latest) 下载 Source code (zip)，它就是包含完整公开文件的安装包。解压后选择：

```text
python install.py --host codex
python install.py --host dsh
python install.py --host both
```

Python 3.11+。安装器复制六个完整技能并添加化学默认入口；原有不同内容先比较，--replace 会先备份。自选宿主目录、--target、--no-defaults 的说明见 install.py --help 和迁移文档。安装器自身会做文件完整性检查。

## 先配置基础能力，再补专业软件

```text
python tools/workbench.py setup --profile foundation --apply
python tools/workbench.py setup --profile spectra --apply
python tools/workbench.py setup --profile thermo-raw --apply
```

先检查并复用现有配置，用 --data-dir 选择数据盘、--python 指定已有解释器。结构识别需要时选 ocsr；已有 Ketcher 可复用。Gaussian/ORCA/SHELX 等使用目标机已有合法软件，GROMACS 对新分子需要对应拓扑和参数；集群为可选项。分享的是方法、脚本、模板和配置工具，不捆绑作者程序、账号或样品。

## 学术支持保持收敛

学术研究负责找文献、SI、条件、先例和引文核验。学术写作默认从 39 项收敛到 7 项：论文、润色、审稿回复、开题、学位论文、Word/PPT 和共享资源。32 项统计/机器学习/海报/专利及重复成品管线退出默认安装包，知识索引和原件恢复见 [可选方法](skills/huangjt-academic-writing/references/optional-methods.md)。它们完整保留在本地及 v1.1.0 固定版本，按需恢复，不重新注册平级技能。

## 本次交付状态

v1.2.0 按用户要求先整理、打包和发布，未追加完整回归或迁移验证。本轮此前已经完成的小型本地 Gaussian、xTB、真实 Thermo/Bruker 读取记录与尚未重跑的部分见基础功能文档；不能把安装、准备输入和完整科学验收混为一谈。第三方来源与许可保留在各技能及 THIRD_PARTY.md。
