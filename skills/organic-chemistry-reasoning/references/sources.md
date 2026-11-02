本文件保留2026年10月29日纯方法版的来源记录。2026年11月2日融合版另加入 modules 中的工具与专门方法，实际范围、归属和引用见 absorbed-modules.md；旧版“不含外部代码”的描述仅适用于此前版本。

# 方法来源与能力边界

更新日期：2026-10-29。本包是针对有机化学科研讨论重新组织的方法说明，非任何上游技能的完整副本；不包含外部仓库代码、模型、数据或第三方论文全文。

## 本地来源

- organic-chemistry-assistant及机理参考：结构先行、原子/电荷守恒、电子移动、文献先例分级。
- scxrd-refinement的practice-lessons和solve-single-crystal：输入分级、模型对照、单晶历史实践边界。
- spectrum-analyzer、matchms、nmrglue：数据类型、元数据、数值处理与鉴定的职责边界。
- huangjt-computational-chemistry及assistant：以任务终点选择方法、稳定构象ID、驻点验收、构象覆盖与可比能量。
- Nature检索/精读类技能：主张—原文定位、SI核对、未报告与阴性证据区分。

其中单晶与构象的特定教训有本地实践记录支持。本包新增的空间/位阻、核磁联合鉴定、实验复盘和反应选择性框架，主要是通用方法的整理；不代表这些手段已全部在个人项目中验证。

## GitHub参考与筛选

本次在线读取了以下原始仓库页面，未安装或执行其内容。链接指向活动分支，后续可能变化；没有把它们描述成已锁定版本。

| 来源 | 借鉴或用途 | 本包的处理 |
|---|---|---|
| [agent-almanac / interpret-nmr-spectrum](https://github.com/pjt222/agent-almanac/blob/main/skills/interpret-nmr-spectrum/SKILL.md) | 由一维到二维相关组织核磁信息；页面标注MIT | 只借鉴组织思路。未照搬J值表或固定偏差阈值；收紧HMBC、NOE及构型结论边界 |
| [K-Dense / nmrglue](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/nmrglue/SKILL.md) | 已校准1D FID处理范围、定量条件与验证界限；页面标注MIT | 保留处理不等于鉴定的分工，未复制脚本或厂商格式可用性声明 |
| [K-Dense / experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/experimental-design/SKILL.md) | 真实独立重复、批次和因素交互 | 只用于有机反应优化的设计原则，不引入不相干研究流程 |
| [Morfeus](https://github.com/digital-chemistry-laboratory/morfeus) | 提供分子几何/位阻描述符，README列出Sterimol、埋藏体积等 | 作为可选量化后端列出；它是软件库，并非本包必需的skill |

外部技能是方法线索，科学结论仍需原始数据和适用的文献。第三方仓库未经本次完整代码审计，未因能读取文档就宣称后端可靠可用。若以后直接复制第三方文件，需另核对仓库许可证并保留所需声明。

## 执行扩展：只列举，暂不放入

| 执行内容 | 可能需要的依赖/条件 |
|---|---|
| 自动读坐标、映射、几何批处理和对齐 | RDKit、Gemmi、ASE或其他适配解析器；简单笛卡尔几何也可用通用计算工具 |
| Sterimol、埋藏体积、锥角等 | Morfeus等专用库，且须明确原子/坐标系和参数；本次未核验本机是否安装 |
| 构象、能量、电子结构与竞争过渡态 | 适合任务的采样/量化软件，参数化、程序许可和计算资源 |
| 原始NMR/FID、复杂谱模拟、计算谱统计 | nmrglue或其他谱学后端；原始格式支持、采集参数、校准；相应计算统计软件 |
| LC/GC定量、LC-MS特征和谱库搜索 | 仪器导出/转换器、校准及对应处理库/数据库 |
| DOE矩阵与统计建模 | 合适统计环境，且事先明确响应、因素和独立重复 |
| 单晶还原、解结构、精修与在线验证 | 对应衍射程序、适配环境及必要授权 |

纯文本规则可以迁移；自动化运行能力需按目标电脑单独核验，不把安装技能视为配置后端。
