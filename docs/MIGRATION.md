本版结构：四个化学核心优先；写作仅七个默认模块，32 个可选方法见写作 references/optional-methods.md。谱文件基础可配置 workbench.py setup --profile spectra/thermo-raw；实际入口见 CORE_ACCEPTANCE.md。本次按要求跳过后续完整验证。

# 在另一台电脑恢复能力

## 先安装完整六技能
下载最新 release，解压后运行 python install.py --check，再选 --host codex、dsh 或 both。安装器复制六个完整文件夹，包括 modules、scripts、references、assets、能力目录和自配置工具；没有把六技能变成空路由。已有不同版本先比较，--replace 会保留备份。源目录保留，便于查看 CATALOG 和版本更新。

## 优先建立基础层
在仓库根目录运行下列命令；安装后的有机核心内 scripts/workbench.py 提供同一入口，因此只迁移六个目录也可配置。

```text
python tools/workbench.py setup --profile foundation
python tools/workbench.py setup --profile foundation --apply
python tools/workbench.py setup --profile ocsr --apply
python tools/workbench.py verify --output 自选的验收目录
python tools/workbench.py search 机理
```

计划输出显示已有解释器和缺包。优先复用，缺包才在数据目录新建环境，不为满足可选功能修改原科研环境。--data-dir 指定数据盘，--python 指定现有 Python。默认运行脚本不安装，--apply 才进行选定配置。配置文件记录本机解释器和程序路径，不照搬作者盘符。请用配置报告的解释器执行结构 CLI。

MolVec 是轻量离线 OCSR，必要的便携 Java 自动从 Eclipse Adoptium 官方接口取得并校验。工具输出候选 MOL/SMILES 和来源哈希；对照原图和重新绘图核对后采用。大模型、整条反应图解析和缩写/立体化学保证不在这项基础验收范围。

## 交互编辑与完整结构工具链
已有 Ketcher 时用 --ketcher-dist 指定含 index.html 的前端，配置不会自动打开桌面。需要安装完整开源 codex-organic-chem 工具链时，先 python tools/workbench.py fetch-source organic，使用返回的固定版本目录；其 pyproject 当前要求 Python 3.12，应在合适环境安装，不改变现有默认 Python。

上游 integrations/ketcher 含 package.json；在有 Node/npm 的目标机运行 npm install 和 npm run build，生成的 dist 可配置为 CODEX_CHEM_KETCHER_DIST。优先已有可用 Node；缺少时按官方平台支持安装。需要实际交互编辑时，再用该工具链的 input-review/structure-review 入口与本地服务；用户修改结果作为结构真源。商用 ChemDraw 等按用户授权另配。

## 按任务添加专业层
setup 的 spectra、crystal、documents 配置只提供对应 Python 基础。实际运行先读核心 CAPABILITIES 和具体模块 WORKFLOW：Gaussian/ORCA/SHELX/Olex2/DIALS、厂商转换器、谱库、数据库与账号分别核实。集群是可选层，明确远端运行任务才配置调度和认证。科学判断、资料加载和普通知识问答不因后端缺失而停摆。

## 未随包的原件仍可恢复
fetch-source 支持 hpc、office、organic、paper、conformer、crystal、ars、nature，下载固定提交到自选数据目录，不执行上游安装器，不增加平级技能。CATALOG、PRESERVATION 与各 EXTERNAL_RESOURCES 解释具体位置。上游测试、评测数据或论文绘图素材有单独来源，不能把它们是否随包等同于主方法是否存在。

## 自己的另一台电脑
“个人完整迁移包”包含本地六个主技能的完整副本，保留本地原始模块、脚本和经验引用，安装前同样有清单验证。它供本人迁移，不作为公开 release；本机绝对路径需目标机重新绑定，模型/语料/授权程序不会自动搬运。六技能之间按样品、原子/构象 ID、方法条件和证据来源交接。
