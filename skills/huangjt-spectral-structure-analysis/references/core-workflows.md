# 实际文件到解谱的基础入口

read_spectral_file.py 直接读取完整 Bruker fid/ser 采集目录、Bruker pdata 处理谱、Varian 目录、NMRPipe、mzML/mzXML/MGF、JCAMP 和带表头 CSV。Bruker 一维/二维 pdata 保留原处理元数据，仅在真实 SI/SF/SW_p/OFFSET 支持时导出存储坐标对应的 ppm 轴；没有执行新的溶剂校准。

Thermo/Finnigan RAW 先从文件头识别，再用目标机已有或官方安装的 ThermoRawFileParser 转为 mzML 并读取，保留转换记录、扫描级信息、峰表和源文件哈希。默认不做原厂峰提取，--centroid 明确选择原厂峰提取；两种结果不能混为同一处理版本。同步目录有锁冲突时使用校验相同的独立工作副本，不改原始 RAW。

Bruker ZIP 先在独立目录解压，按 acqus/fid/ser、procs/1r/2rr 定位实验；包含多实验时按谱种和采集参数选取，不混淆 HSQC/HMBC/COSY。读取原始 FID 不等于自动完成数字滤波、相位、基线、NUS 重建或积分：process_1d.py 支持显式参数的 1D 数值处理，二维沿实际采集/处理方案核对。

读取后接主技能的实验流程和候选判断：核磁积分/裂分/相关，MS 电荷/加合离子/同位素/碎片，反应来源交有机，预测核磁/J/构象交计算。MS1 无法冒充 MS/MS；峰响应不能直接换算产率或含量。已有原始数据和处理谱统一校准时保留处理历史，不复制旧样品的偏移量。

不能通用读取的情况要具体说明：其他品牌 .raw/.d 先判定格式并选择对应转换器；Mnova 文档用已授权软件导出支持格式。单凭扩展名不宣称已读取。软件依赖由 workbench spectra/thermo-raw 配置，安装后用实际文件验收。
