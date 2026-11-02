# 基础能力与迁移

## 新电脑的顺序
先保留并复用现有软件，安装六个技能与默认规则；基础层优先配置结构识别、绘制编辑、MOL/SDF/SMILES 转换、分子式和精确质量。随后按当前任务配置解谱、单晶、文献或文档依赖。Gaussian、ORCA 等专业软件按其授权处理，集群为可选项。

在本技能目录中找到 scripts/workbench.py（有机核心）或到同级 organic-chemistry-reasoning/scripts/workbench.py。它随六技能迁移，无需原作者路径或额外顶层技能。

```text
python scripts/workbench.py setup --profile foundation
python scripts/workbench.py setup --profile foundation --apply
python scripts/workbench.py setup --profile ocsr --apply
python scripts/workbench.py verify --output 自选的测试结果目录
python scripts/workbench.py search 核磁
```

上述命令在有机核心目录运行；仓库根目录也提供 tools/workbench.py 同等入口。默认只检查/列计划；--apply 安装选定集合。缺包时新建专用环境，已有可用环境优先复用；不修改不相关科研环境。--data-dir 指定程序/环境目录，--python 指定现有解释器。配置输出会显示实际解释器，后续用该解释器运行脚本。

基础 Python 需 3.11+；codex-organic-chem 完整外部工具链当前需 Python 3.12，按来源 pyproject 另选环境。foundation 支持 RDKit/Pillow；spectra、crystal、documents 是可选配置，不代表对应全部外部软件已验收。ocsr 配置 MolVec 和必要的便携 Java，下载留校验信息；不要求大型深度学习模型。Ketcher 已有前端时可传 --ketcher-dist 复用，不自动打开浏览器。

结构操作 examples：
```text
python scripts/structure_cli.py info "CCO"
python scripts/structure_cli.py draw "CCO" --output ethanol.svg
python scripts/structure_cli.py convert "CCO" --output ethanol.mol
python scripts/structure_cli.py ocsr cropped-molecule.png --output candidate.json
```

输入图片留原件；识别结果重新绘图核对键、缩写和立体化学。MolVec 不解析整条反应图，合成图片自检不代表真实论文图准确率。复杂图可按需从原仓库安装 MolScribe/DECIMER/OpenChemIE，保留各自环境和模型版本。

## 软件和原始资源未随包时
查看本技能 CAPABILITIES.md 和模块 WORKFLOW，保留知识与获取路径。scripts/workbench.py fetch-source 支持 hpc、office、organic、paper、conformer、crystal，按固定提交下载完整上游到数据目录；不执行安装器、不注册额外平级技能。运行时依赖与原始模块资料属于不同对象。

个人电脑迁移可使用另外生成的“个人完整迁移包”，包含本地完整六技能和模块；它与公开包分别维护，个人路径/历史不上传 GitHub。模型、商业程序、私有语料和账号仍用目标机已有配置或按需安装；不能因未随包而删掉其方法与工具线索。
