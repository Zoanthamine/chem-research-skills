# 四核心基础功能与当前状态

## 单晶：可以从原始帧处理衍射数据
DIALS 支持的原始帧和完整几何可按 import → find_spots → index → refine → integrate → symmetry/scale → export 处理，再进入解结构精修。具体命令、阶段日志与输出在单晶 references/dials-to-olex2.md 和 scripts/dials_stage.py。主核心有 21 项 Python 工具、26 份主要方法参考；并不是只有一个来源子模块。

本轮确认本机 DIALS 3.30 入口可用，保留此前真实工作经验；没有在本次发布前重新还原一套用户衍射数据。只有 CIF 或校正 HKL 不能重建丢失像素和重新积分。

## 计算：本地采样 → DFT → 核磁
local_sampling.py 准备/执行 xTB MD 或已有对应 GRO/TOP/MDP 的 GROMACS 任务；采样帧需检查连接/立体化学，优化、去重与排序后再选 DFT 候选。GROMACS 新分子必须重新参数化，不能复用旧样品 RESP/拓扑。

prepare_nmr_jobs.py 生成 opt/freq、GIAO 或指定 FC 基组任务；run_gaussian_nmr.py 可调用目标机的 Gaussian，先确认优化/频率再运行性质并导出原始屏蔽。核磁方法/基组、溶剂、标度或参照和权重要匹配；Bally/DU4 及原基组保留在 nmr-coupling.md、assets/basis 和 coupling_postprocess.py。

本轮用已有软件完成了单一起点正丁烷 1 ps xTB MD，以及小型水分子的本地 Gaussian 优化、频率、GIAO 屏蔽测试。它们验证这些调用路径，不证明任意分子都已完成构象覆盖或核磁预测。GROMACS 本轮确认程序入口，未再做新体系参数化和完整搜索；既有分子的经验保留。

## 解谱：实际文件读取
read_spectral_file.py 读取完整 Bruker fid/ser 和 pdata、Varian、NMRPipe、mzML/mzXML/MGF、JCAMP/CSV；Thermo/Finnigan RAW 从文件头识别，经 ThermoRawFileParser 转换并保留日志和哈希。默认保留轮廓数据，--centroid 显式选择原厂峰提取。遇同步锁时使用校验相同的工作副本，原始数据不变。

此前已经跑通本机真实 Thermo RAW、Bruker 一维和二维处理谱；新增读取入口也完成了这些真实格式读取以及合成 Bruker/Varian/NMRPipe/mzML/MGF 测试。读取、重新处理、定量和结构归属分别进行。ZIP 先解到独立目录定位实验；多实验不可静默挑一份。Mnova、其他品牌 RAW/D 依实际软件或转换器处理，不根据扩展名假称通读。

## 有机：围绕问题组织证据
结构识别/绘制转换、真实结构/原子映射、机理与重排、选择性、保护基和后处理均由有机核心组织；实际谱图交解谱，构象/预测交计算，衍射模型交单晶，先例交研究。保留观察、竞争解释、限制和区分性对照，写作整理结果。

## 发布前验证范围
按用户本次要求，完成以上已有工作后跳过后续完整回归、迁移测试及额外科学验证，直接打包发布 v1.2.0。新增整理和所有组合路径尚未逐项重测；不沿用 v1.1.0 CI 作为本版完整通过声明。
