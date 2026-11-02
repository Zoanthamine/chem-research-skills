# 5 分钟上手

目标：在**另一台电脑**上得到和作者相同的使用体验——六个技能可被发现、化学任务自动路由、基础后端可自检。

不需要先装 Gaussian/ORCA/DIALS 等专业软件；安装、自检和结构/格式基础能力都能先跑起来。

## 你会得到什么

| 得到 | 说明 |
|---|---|
| 六个技能入口 | 单晶、计算化学、解谱、有机推断、学术检索、学术写作 |
| 默认路由 | 一段受管规则写进宿主 `AGENTS.md`：说“修单晶/算核磁/解谱/有机/找文献/写作”就会进对应核心 |
| 安装标记 | `skills/.huangjt-chemistry-install.json`，记录版本与六技能指纹，便于升级/回滚判断 |
| 自检工具 | `tools/doctor.py`：宿主、安装、完整性、Python 依赖、外部软件、下一步命令 |
| 后端配置器 | `tools/workbench.py`：按 profile 在数据目录建独立环境，不动你现有的 Python |
| 逐文件索引 | `docs/INVENTORY.md` / `inventory.csv` / `inventory.html`：每个文件是干什么的 |

## 第 1 步：拿到源码并校验

从 [Releases](https://github.com/Zoanthamine/chem-research-skills/releases) 下载 **Source code (zip)**，解压到短路径（Windows 建议 `D:\chem-skills`，避免超长路径）。

```bash
cd chem-research-skills
python install.py --check
# {"verified_files": 2704, "skills": [...], "installed": false}
```

需要 Python 3.11+。`--check` 只核对 `MANIFEST.json`，不写任何文件；对不上就重新解压，不要继续。

## 第 2 步：先看计划，再安装

```bash
# 看计划（不写文件）
python install.py --host dsh --dry-run

# 安装：DSH / Codex / 两个都要 / 自动检测
python install.py --host dsh
python install.py --host codex
python install.py --host both --smoke
python install.py --host auto --dry-run
```

| 宿主 | 技能目录 | 全局规则 |
|---|---|---|
| DeepSeek Harness | `$DSH_HOME/skills`（默认 `~/.dsh/skills`） | `$DSH_HOME/AGENTS.md` |
| Codex | `$AGENTS_HOME/skills`（默认 `~/.agents/skills`） | `$CODEX_HOME/AGENTS.md` |

自定义位置：`python install.py --host dsh --target D:\chem-skills\installed`。

安装器只做四件事：校验 → 复制六个文件夹 → 写安装标记 → 注入受管规则。已存在同名但内容不同的技能时会**拒绝覆盖**；确认后加 `--replace`，旧目录会先移动到 `chemistry-skill-backups/<时间戳>/`。

## 第 3 步：自检

```bash
python tools/doctor.py
```

输出分四段：仓库完整性、宿主与安装状态、Python/依赖 profile、外部专业软件。最后给出“下一步”命令。

- ✅ 完整 / 已装 6/6
- ⚠️ 依赖缺：按提示跑 `tools/workbench.py setup --profile ... --apply`
- — 外部软件未装：正常，按任务需要再装（见下方“软件从哪来”）

## 第 4 步：配置基础后端（可选，但推荐）

`--apply` 会在数据目录下建独立虚拟环境并安装，不动你现有的 Python：

| profile | 安装内容 | 用在哪 |
|---|---|---|
| `foundation` | rdkit、Pillow | 结构式识别/绘制/转换、分子式与精确质量 |
| `spectra` | numpy、scipy、matplotlib、nmrglue、pyopenms | NMR/MS 文件读取、处理、绘图 |
| `thermo-raw` | pyopenms | Thermo `.raw` → mzML 转换链路 |
| `crystal` | gemmi、numpy、requests | CIF/HKL 处理 |
| `documents` | python-docx、python-pptx、pypdf、Pillow | Word/PPT 成品 |
| `ocsr` | rdkit、Pillow + MolVec + Java | 离线图片识图（可选） |

```bash
python tools/workbench.py setup --profile foundation --apply
python tools/workbench.py search nmr            # 查内置模块
python tools/workbench.py search --optional     # 查未随包分发的 32 个可选模块
```

## 软件从哪来

| 类别 | 例子 | 谁负责 |
|---|---|---|
| 开源、可自动配置 | rdkit、nmrglue、pyopenms、MolVec、ThermoRawFileParser | `workbench.py setup --apply` 或 doctor 提示 |
| 需合法授权 | Gaussian、ORCA、Mnova、ADF/AMS | 用你已有的授权版本；包装不含程序 |
| 需单独安装 | DIALS、SHELXL/SHELXT、PLATON、GROMACS、xTB、Multiwfn | 按核心文档安装后，把路径写进环境变量（见 `docs/WORKFLOWS.md`） |
| 可选 | 集群调度、GPU 构建、数据库 | 按需，默认不配置 |

## 第一次任务

新开一个会话（让技能目录被重新发现），然后直接用自然语言：

- “帮我检查这个 CIF，有没有 A 级警报，能不能交付”
- “用这套构象做核磁计算，选合适的基组，和实验值对比”
- “读一下这个 Bruker 文件夹和这个 Thermo raw，帮我归属目标峰”
- “这个反应为什么主要给这个产物，有没有重排可能”
- “找一下这个底物的类似反应和 SI 条件”
- “把这次分析整理成组会 PPT”

## 更新、卸载与回滚

- 更新：解压新版 → `python install.py --check` → `python install.py --host dsh --replace`（旧版自动备份）
- 只撤默认路由：删掉 `AGENTS.md` 里 `<!-- huangjt-chemistry-defaults:begin -->` 到 `end` 之间的段
- 卸载技能：删除六个技能目录和安装标记即可；备份在 `chemistry-skill-backups/`
- 恢复可选模块：`python tools/workbench.py restore-optional <module> --skills-root <已安装技能目录>`

## 边界

安装完成只代表**文件完整、入口可发现**；不代表任意分子/数据都能一键得到科学结论。每个核心能做什么、哪些步骤已验证，见 `docs/CORE_ACCEPTANCE.md` 与各技能 `CAPABILITIES.md`。遇到问题先看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)。