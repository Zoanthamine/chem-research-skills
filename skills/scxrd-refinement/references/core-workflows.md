# 单晶基础功能：DIALS → 解结构 → 精修

本核心的主体是 scripts 和 references，不是单个来源辅助模块。原始衍射帧可按输入格式与几何支持进入 DIALS：导入、选点、索引、晶格/对称判断、几何精修、积分、标度、晶胞与不确定度、导出 SHELX/SADABS，再衔接 SHELXT/SHELXL/Olex2。已有可靠 HKL 直接从解结构/模型精修进入。

实际命令、输入输出与证据检查在 [DIALS 到 Olex2](dials-to-olex2.md)、[工具入口](dials-tools.md)、[还原判断](dials-decisions.md)。scripts/dials_stage.py 能实际执行各 DIALS 阶段并保留命令、日志和哈希；dials_audit/screen/absorption 分别用于几何/强度、双重证据筛选、吸收分量核验。新格式先验证像素、方向和几何，不能仅凭后缀判断可还原。

专业分析还包括：配体和连接、空间群竞争、无序和占有率、特殊位置与多重性、孪晶协议、H/质子转移、ADP、弥散溶剂、CIF/FCF 配套和警报调查。入口表按实际证据选择，所有参考在 CAPABILITIES 完整列出。只有 CIF 或处理后的 HKL 无法恢复丢失的原始衍射像素。

分享包同时保留主程序、25 份以上主要方法参考和来源扩展知识；来源模块的“0 个额外脚本”不代表本核心没有工具。DIALS 是可选还原分支，常规精修不强制重新还原。

官方对照：https://dials.github.io/documentation/tutorials/small_molecule_tutorial.html 。版本参数以目标机帮助和当前实验数据为准，不照搬教程晶胞或空间群。
