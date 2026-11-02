# 单晶辅助知识与原始工具获取

本模块保留输入分级、配体核对、孪晶调查和验证交付的知识；主入口为 scxrd-refinement。完整原始文件在作者公开仓库和本机原件中保留，公开包不会把该模块的缺席伪装成能力已经完整安装。

## 原始资料与工具
固定来源：https://github.com/owenxyzhang-seseTJ/solve-single-crystal-skill/tree/2dc5c8d29c887e877f03bd71da52c377f47d9c84

在有机核心目录运行 python scripts/workbench.py fetch-source crystal --data-dir 自选数据目录，可取得完整上游。个人完整迁移包同时保留本机原件。原始目录含 data-gates、refinement-playbook、twinning、validation-delivery 四份参考，以及 inventory_crystal_input、prepare_ligand、validate_crystal_package、fix_fcf_for_twinrotmat 和配体启动脚本。取得源文件后先检查实际参数与程序兼容性。

本主技能 scripts/inventory_crystal_input.py、prepare_ligand.py、validate_crystal_package.py 已提供前三项可移植工具，不依赖原辅助目录的脚本副本。更多推理与决策已在主技能 references/solution-and-ligand.md、refinement-decisions.md、twin-investigation.md、package-audit.md 和 applied-workflows.md 具体保留。

## 输入分级与配体
原始像素帧支持调查索引、积分、背景和多晶畴；未合并观测支持保留批次与几何的标度/吸收调查；可靠校正 HKL 支持解结构精修；只有 CIF/RES 时做模型诊断。不同层级不可跨越声称已完成的处理。配体的连接、立体化学、电荷和原子映射独立于衍射模型核对，优化几何只作参考。

## 精修、孪晶与验证
从当前父版本原样复现，按明确问题做可追踪对照；无序组分、占有率、多重性和 ADP 一起检查。孪晶律需晶格与反射证据；非重叠组分一般不能由合并 HKL 恢复。HKLF 4/5、TWIN/BASF、空间群和反射协议要匹配，不能以降低 R 为由强行选择模型。

TwinRotMat 格式适配只作用于诊断副本：检查当前 FCF 的标签、权重来源、波长、强度/振幅定义和 PLATON 版本；没有真实来源的缺项保持未知。原格式转换脚本必须从原件获取后检查适用条件，不在缺失时静默跳过或编造字段。诊断输出不能冒充正式提交 FCF。

最终 CIF/FCF、模型、强度与验证报告绑定同一轮；核对组成、氢、ADP、连接、残差、权重、嵌入记录和外部依赖。交付时提供原始数据、复跑材料、哈希、采用理由、保留警报与限制。是否需要额外去孪晶归档取决于实际数据与用途，不把原模块的固定动作提高为所有任务的要求。

## 随包知识章节

- [输入与数据](references/data-gates.md)
- [精修对照](references/refinement-playbook.md)
- [孪晶调查](references/twinning.md)
- [验证交付](references/validation-delivery.md)

主技能自己的 21 项 Python 工具、DIALS 分阶段执行和专业参考均在上层 CAPABILITIES；不以本来源子模块的脚本数替代整个单晶核心的能力。
