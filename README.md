# Huangjt 化学科研技能

四个独立化学核心，配合两个学术技能。在Codex和DeepSeek Harness中按问题加载方法与工具，减少重复入口。

| 日常说法 | 主技能 |
|---|---|
| 修单晶、处理警报、无序孪晶、CCDC包 | scxrd-refinement |
| 核磁计算、构象退火、Gaussian、轨道、TS/IRC | huangjt-computational-chemistry |
| 解谱、目标产物在哪、原料副产物、多谱归属 | huangjt-spectral-structure-analysis |
| 有机、这个反应做成了吗、机理、位阻、选择性 | organic-chemistry-reasoning |
| 找文献、SOP、SI条件、读论文、DOI、Zotero | huangjt-academic-research |
| 写作润色、汇报、科研图表、论文PPT/Word | huangjt-academic-writing |

## 在另一台电脑快速配置

把下面一句话发给那台电脑的AI助手，由它按[首次配置流程](docs/FIRST_RUN.md)检测现有条件、安装六技能并自主选择必要的软件与环境：

> 请读取 https://github.com/Zoanthamine/chem-research-skills 的首次配置说明，检查这台电脑并配置六大技能、将四个化学核心设为默认，结合我的日常科研需求自主选择下载和安装所需软件及独立环境，优先复用已有配置，只在需要账号、付费授权或系统权限时让我处理，并完成验证和简明使用说明。

## 安装

下载[最新版安装包](https://github.com/Zoanthamine/chem-research-skills/releases/latest)，解压后在目录中运行以下之一。需要Python 3.11或更新版本，安装器只使用标准库。

```text
python install.py --host codex
python install.py --host dsh
python install.py --host both
```

Windows也可双击install-codex.cmd或install-dsh.cmd。自定义DSH数据目录：`python install.py --host dsh --dsh-home D:/DSH/Data`。已有同名且内容不同的技能会拒绝覆盖；比较后可用`--replace`，原文件会先移到带日期的备份目录。

默认会在所选宿主的全局AGENTS.md加入一段可识别、可重复更新的化学默认规则，让四核心优先处理化学任务，并由两个学术入口承接证据和成品。其他项目内容保留。只安装技能不添加默认规则：`--no-defaults`。精确自选技能目录使用`--target`，该选项只适用于单个宿主。

Codex技能默认安装到AGENTS_HOME/skills或~/.agents/skills；其全局说明使用CODEX_HOME/AGENTS.md或~/.codex/AGENTS.md。DSH使用DSH_HOME/skills或~/.dsh/skills。若产品没有立即刷新技能列表，新开聊天或重新载入。

也可以先克隆再安装：

```text
git -c core.longpaths=true clone https://github.com/Zoanthamine/chem-research-skills.git
cd chem-research-skills
python install.py --check
python install.py --host both
```

## 使用与联动

不必记住英文技能名，可直接说“解谱”“核磁计算”“修单晶”“找反应条件”。“看看这个、分析一下、继续”根据当前附件和化学问题继承入口。一个问题先用一个主技能，需要另一类证据时再交接；不会为简单问题加载整套流程。

例如“这个反应做成了吗”：有机核心组织问题，波谱核心检查原料、目标物和副产物，研究入口查先例；计算确能区分候选时才执行计算，写作入口复用核实后的图表形成汇报。逐证据区分实测、预测、文献和用户确认。

## Codex与DSH

六个技能的核心是宿主无关的Markdown方法、相对资源和普通命令行脚本。宿主适配表在各技能references/host-compatibility.md。使用现有的文件、命令、检索和Office工具，不依赖Codex私有API。中文任务优先选择对应核心；缺少某后端不阻止知识讨论。

安装技能不等于安装全部科学软件。本仓库不捆绑SHELX、Gaussian、ORCA、xTB、DIALS、模型、数据库订阅或许可证；只在实际任务需要时配置相应后端。普通数值脚本、DIALS和逆合成可能需要不同环境，依脚本--help和方法参考选择。不要整批重跑模块自带的上游安装器。

## 内容与许可

四核心保持完整和独立。78个专门方向按需放入内部modules，入口为WORKFLOW.md，避免注册成更多同级技能。公开版保留有分发依据的源模块；8个未能确认原件分发条件的方向使用本项目独立整理的通用方法。本机完整资料不随公开版上传。ARS的上游维护测试、held-out评测和原始评测运行记录不在发布版内，运行方法、工作流、契约和工具保留；不将上游整仓发布门槛当作用户任务的前置条件。

原创部分MIT，第三方模块各按原许可；ARS文档和适配内容含CC BY-NC 4.0非商业限制。具体见[THIRD_PARTY.md](THIRD_PARTY.md)及[SOURCE-LICENSES.json](SOURCE-LICENSES.json)。外部科学软件的许可另行适用。

## 验证

`python install.py --check`验证文件哈希和六个入口；`python -m unittest discover -s tests`检查安装、全局规则、覆盖保护和篡改拒绝。CI还运行现有单晶辅助测试与波谱数值自检。它们不替代真实样品精修、量化计算或文献原文核验，也不承诺模型每次自动选择技能。
