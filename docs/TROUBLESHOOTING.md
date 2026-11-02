# 常见问题与处理

先跑 `python tools/doctor.py`，它会指出大多数问题的位置。下面是按症状查的处理办法。

## 安装

**`install.py --check` 报 `Checksum mismatch` / `Missing/unsafe file` / `Unexpected package files`**

发布包被改动过（复制时混入缓存、编辑器改了行尾、解压不完整）。重新从 Releases 下载 Source code (zip)，解压到干净目录再跑。不要对官方包手工改文件；改了就用 `python tools/manifest.py --write` 重新生成账本，但那样已不是发布版。

**`FileExistsError: Existing different skill`**

目标目录已有同名技能且内容不同。先比较（`git diff --no-index` 或直接看文件），确认要替换时：

```bash
python install.py --host dsh --replace
```

旧目录会移动到 `chemistry-skill-backups/<时间戳>/skills/<name>`，不会递归删除。

**装完在新会话里看不到技能**

- 需要**新开会话**或刷新宿主的技能目录缓存；
- 确认 `python install.py --host dsh --dry-run` 里的路径就是宿主实际读取的目录（`DSH_HOME`、`AGENTS_HOME`）；
- 用 `python tools/doctor.py --skills-dir <目录> --json` 看“找到/缺少/内容不同”。

**`AGENTS.md` 里的规则重复或不完整**

受管块用 `<!-- huangjt-chemistry-defaults:begin -->` / `end` 标记。重复：删掉多余块再运行安装器；不完整（只有 begin）：手工补 end 或从备份恢复 `instructions/` 下原文件。

**不想改全局规则**

`python install.py --host dsh --no-defaults`：只装技能，不写 `AGENTS.md`。

## Python 与依赖

**`python` 不是 3.11+**

安装器会明确报错。装 3.12/3.13 后重跑；多个 Python 并存时用绝对路径调用，例如 `C:\Python312\python.exe install.py --host dsh`。

**`workbench.py setup --apply` 卡住或失败**

- 网络：pip 需要能访问包源；公司/校园网可先设镜像 `PIP_INDEX_URL`。
- 权限：不要用管理员权限装到共享环境；配置器默认在数据目录建独立 venv。
- 依赖冲突：它**故意**不修改现有环境。冲突就换 profile 或换数据目录（`--data-dir`）。

**profile 已“安装”但 doctor 仍显示 ⚠️**

不同 Python 解释器。doctor 检查的是**当前运行 doctor 的解释器**；用配置器记录的 python 重跑：

```bash
<workbench venv>/python tools/doctor.py
```

## 专业软件

**doctor 里 DIALS/Gaussian/ORCA/SHELX 显示 `—`**

未安装或不在 PATH。两种做法：

1. 装好后把可执行文件目录加入 PATH；
2. 或设置环境变量，doctor/脚本会优先使用（布尔值表示是否必需）：

| 软件 | 环境变量 |
|---|---|
| DIALS | `DIALS_BIN` |
| SHELXL/SHELXT | `SHELXL_EXE` / `SHELXT_EXE` |
| PLATON | `PLATON_EXE` |
| Gaussian | `GAUSSIAN_EXE`（或 `G16_EXE`） |
| ORCA | `ORCA_EXE` |
| xTB | `CODEX_CHEM_XTB_PATH` |
| GROMACS | `GMX_BIN` |
| ThermoRawFileParser | `THERMO_RAW_FILE_PARSER` |

**“软件在，但脚本说找不到”**

GUI 安装的程序通常不写 PATH。检查 doctor 的“外部软件”行是否显示路径；没有就设上面的变量。包装里不含任何商业程序或授权。

## 数据与格式

**Thermo `.raw` 打不开**

需要 ThermoRawFileParser（`python tools/workbench.py setup --profile thermo-raw --apply`），且原始文件被仪器软件占用时先复制一份（读取脚本会校验哈希，使用工作副本）。

**Bruker 文件夹读不到**

传整个实验目录（含 `fid`/`ser`、`acqus`、`pdata`），不要只传处理后的谱图；多实验时明确指定哪一个，不要静默挑一个。

**二维谱/相位/NUS**

读取与处理是两件事。读取脚本只做读取与元数据保留；相位、基线、NUS 重建要按解谱核心的流程单独判断。

## 完整性维护（维护者）

```bash
python tools/manifest.py --check      # 账本是否过期（CI 也跑）
python tools/manifest.py --write      # 改了文件后重新生成
python tools/inventory.py --check     # 索引是否过期
python tools/inventory.py --write     # 重新生成逐文件索引
```

CI 会在账本或索引过期时失败，这是有意的：发布包必须和审查过的内容一致。

## 回滚

- 技能：从 `chemistry-skill-backups/<时间戳>/skills/` 复制的对应目录
- 全局规则：从 `chemistry-skill-backups/<时间戳>/instructions/` 恢复 `AGENTS.md`
- 可选模块：`python tools/workbench.py restore-optional <module> --skills-root <目录>`（从 v1.1.0 固定版本恢复，逐个校验哈希）