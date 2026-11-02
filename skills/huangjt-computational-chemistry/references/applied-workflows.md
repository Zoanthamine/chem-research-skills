# 计算方法、模板与实际执行的联动

## 核磁计算或耦合
先明确需要屏蔽常数、标度后的化学位移还是 J，保留结构身份、原子编号、电荷自旋、溶剂温度和实验对应。按 references/nmr-coupling.md 区分不同估计式与适用方法；不同 FC 拟合、屏蔽和位移不可混用。

1. 结构输入和初始几何：modules/rdkit-conf/WORKFLOW.md、scripts/rdkit_conf_helper.py 提供单分子/CSV/SMI、多构象、种子和失败记录。二维回退只用于绘图；力场最低点不是量化自由能最低点。
2. 构象采样：按 references/local-conformers.md 和 modules/hpc-gromacs/ 的拓扑、温控、约束与重启知识建立当前分子任务。记录采样/提帧/聚类/优化条件，不复用别的分子的拓扑或收费软件配置。
3. 优化、频率、单点、屏蔽/J 分阶段衔接：modules/hpc-gaussian/references/ 中的输入矩阵、方法基组、几何电荷自旋、SCF/优化/频率、checkpoint 与错误词典均已恢复。assets/templates 含输入和队列样例；按当前任务检查后使用。
4. 校准与加权：保留每个构象原始数值、匹配的标度参数、温度和权重来源。缺少匹配校准时只交付屏蔽，不自动套近似公式。后处理 CLI 见 references/postprocess-cli.md。
5. 将计算条件、覆盖限制、原子映射、预测值和不确定性交波谱主技能，使用实测谱检验候选，避免把计算一致性写成实测确证。

## 本地、集群和故障恢复
知识讨论使用方法，不启动后端；实际运行遵循 task-preflight。集群是可选执行位置，并不强制所有任务远端化。modules/hpc-orchestration 完整保留 Slurm/PBS/LSF、数组、MPI、scratch、同步、容器、日志、提交回执和重启资料，以及四个 Python 帮助脚本。先通过 --help 核对提交/取消等副作用；未明确提交状态时先查队列，避免重复作业。

Gaussian/ORCA 收敛、驻点类型、TS 模式与 IRC 终点需要分别判断。一个成功退出码或日志末尾文字不能替代结构与科学验收；外部程序按目标机平台和许可证配置。
