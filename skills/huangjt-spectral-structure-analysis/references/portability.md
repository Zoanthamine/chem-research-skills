# 迁移和能力矩阵

将本技能整个文件夹放到另一台电脑的Codex skills目录（用户指定目录优先；默认$CODEX_HOME/skills或~/.codex/skills）。路径均相对本技能，无需保留E盘。Python3.11+建议新虚拟环境：
```
python -m venv .venv
# Windows: .venv/Scripts/python；Linux/macOS: .venv/bin/python
python -m pip install -r requirements-core.txt
python scripts/evidence_cli.py doctor
python scripts/evidence_cli.py selftest
```
上述python应指向虚拟环境，不自动下载安装任何外部软件。requirements-core是可安装兼容范围；本次实际运行版本另存environment-tested.json。包不捆绑解释器/wheel，不声称离线零依赖。doctor只检查模块存在，示例自检才验证已支持数值行为。可选依赖按需安装，二进制和许可证单独迁移。

|能力|需要的条件|本包保留的方法|
|---|---|---|
|结构标准化、精确质量/分子式、绘图|RDKit；datamol/OpenBabel/codex-chem可选|结构身份核对、离子与中性组分区分、候选排除；内置分子式质量命令|
|图片自动识别结构|OCSR模型及推理依赖，需当地验证|未配置时人工目视转录并标明，键/立体逐项定位，与结构文件交叉检查|
|交互式结构修改|Ketcher及本地服务|最终用户修正的结构作为后续真源；编辑器不是本包内置|
|MS/MS批处理、谱库检索|matchms+合法谱库；LC-MS特征处理需pyOpenMS等|加合离子与碎片守恒、匹配证据分级；本包无自带谱库|
|仪器专有原始谱处理|厂商软件/转换器，受许可证及平台限制|优先元数据、转换通用格式；不可假称所有.raw或.mnova能读|
|光谱数值处理、原始NMR|numpy/scipy；FID需nmrglue及采集参数|区分连续谱/峰表、ppm/Hz、统一校准、跨谱追踪|
|量化核磁/J/构象|Gaussian/ORCA/xTB等各自配置|解析可携带结果；不捆绑集群凭据/许可证/编译程序|
|PPT/XLSX整理|目标环境文档工具|可编辑表、逐证据结论；本包不含Codex桌面私有运行时|

本机若已配置science.ps1可继续用它；新电脑不依赖旧绝对路径。禁带密钥、账号、服务器凭据。上游GUI默认不执行；仅显式需要、依赖/软件就绪且授权时使用。

## 数据模式
NOE：NPZ含data二维实矩阵(y,x)、x_ppm与y_ppm一维坐标；必须事先验证轴与校准。JSON配置含signals:{id:[center_ppm,halfwidth_ppm]}及pairs:[[id,id]]。命令：`python scripts/evidence_cli.py noe --input spectrum.npz --config windows.json --output volumes.json`。输出是有符号体积与窗口敏感性，不是距离。
距离：JSON含weights:[...]、distances:[[各构象距离],...]；命令distance返回每一配对的有效距离，输入距离须已确认单位Å与氢编号。
质量：`python scripts/evidence_cli.py mass C27H34O7`。当前支持常用C/H/N/O/S/F/Cl/Br/P/Si及正一价加合离子；不解析盐、同位素标记或任意带电SMILES。

随包 scripts/process_1d.py 来自本机nmrglue技能的MIT标识助手：python scripts/process_1d.py --help。仅校准复FID NPZ或受支持NMRPipe，必须填真实采集参数；示例配置不能直接套实验。Bruker先按真实元数据解码。
通用NOE脚本使用排除信号窗的背景环；本案例历史脚本用外框中位数，故新工具不宣称逐字节复现历史NOE体积，原结果和原脚本均归档。
