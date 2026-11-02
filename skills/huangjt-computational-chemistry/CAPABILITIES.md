# 计算化学与核磁计算：方法与工具

本目录同时列出本主技能自身内容及内部模块。按实际任务选入口；统计用于定位资料。

## 主技能方法

- [absorbed-modules.md](<references/absorbed-modules.md>)
- [applied-workflows.md](<references/applied-workflows.md>)
- [cluster-workflow.md](<references/cluster-workflow.md>)
- [common.md](<references/common.md>)
- [core-workflows.md](<references/core-workflows.md>)
- [experience-maintenance.md](<references/experience-maintenance.md>)
- [foundation-and-migration.md](<references/foundation-and-migration.md>)
- [host-compatibility.md](<references/host-compatibility.md>)
- [integrated-methods.md](<references/integrated-methods.md>)
- [local-conformers.md](<references/local-conformers.md>)
- [local-runtime.md](<references/local-runtime.md>)
- [nmr-coupling.md](<references/nmr-coupling.md>)
- [operations-lessons.md](<references/operations-lessons.md>)
- [postprocess-cli.md](<references/postprocess-cli.md>)
- [runtime.md](<references/runtime.md>)
- [system-integration.md](<references/system-integration.md>)
- [task-language.md](<references/task-language.md>)
- [task-preflight.md](<references/task-preflight.md>)

## 主技能脚本

- [backend_inventory.py](<scripts/backend_inventory.py>) — Inspect configured executable availability without launching software or network.
- [coupling_postprocess.py](<scripts/coupling_postprocess.py>) — Scale one FC protocol at a time; optional signed, explicit conformer weighting.
- [local_sampling.py](<scripts/local_sampling.py>) — Prepare or execute a local xTB/GROMACS sampling job in a new directory. GROMACS requires a reviewed, molecule-specific topology and MDP; this tool never reuses another molecule's R
- [prepare_nmr_jobs.py](<scripts/prepare_nmr_jobs.py>) — Prepare auditable Gaussian opt/freq and NMR inputs from selected XYZ conformers. Does not submit jobs, invent shifts, choose an unverified calibration, or treat xTB energies as DFT
- [run_gaussian_nmr.py](<scripts/run_gaussian_nmr.py>) — Run one prepared conformer's Gaussian stages, preserving inputs and all logs. Opt/freq must finish as a minimum before the separate NMR stage. No scheduler or SSH is used. The call

## hpc-gaussian

[完整流程](<modules/hpc-gaussian/WORKFLOW.md>)

任务：计算化学 高斯 核磁计算 化学位移 耦合常数 优化 频率 过渡态 checkpoint

### 工具

- [assets/templates/gaussian-g16-slurm.sh](<modules/hpc-gaussian/assets/templates/gaussian-g16-slurm.sh>)

### 参考

- [references/checkpoint-restart-and-artifacts.md](<modules/hpc-gaussian/references/checkpoint-restart-and-artifacts.md>)
- [references/cluster-execution-playbook.md](<modules/hpc-gaussian/references/cluster-execution-playbook.md>)
- [references/error-pattern-dictionary.md](<modules/hpc-gaussian/references/error-pattern-dictionary.md>)
- [references/error-recovery.md](<modules/hpc-gaussian/references/error-recovery.md>)
- [references/geometry-charge-spin.md](<modules/hpc-gaussian/references/geometry-charge-spin.md>)
- [references/input-and-link0-matrix.md](<modules/hpc-gaussian/references/input-and-link0-matrix.md>)
- [references/method-basis-and-jobtype.md](<modules/hpc-gaussian/references/method-basis-and-jobtype.md>)
- [references/scf-opt-freq-and-solvation.md](<modules/hpc-gaussian/references/scf-opt-freq-and-solvation.md>)
- [references/workflow-manual.md](<modules/hpc-gaussian/references/workflow-manual.md>)

### 模板

- [assets/templates/gaussian-g16-slurm.sh](<modules/hpc-gaussian/assets/templates/gaussian-g16-slurm.sh>)
- [assets/templates/opt_freq_water.gjf](<modules/hpc-gaussian/assets/templates/opt_freq_water.gjf>)
- [assets/templates/sp_water.gjf](<modules/hpc-gaussian/assets/templates/sp_water.gjf>)

## hpc-gromacs

[完整流程](<modules/hpc-gromacs/WORKFLOW.md>)

任务：构象 退火 分子动力学 拓扑 力场 温控 重启 GROMACS

### 工具

- [assets/templates/gromacs-mdrun-slurm.sh](<modules/hpc-gromacs/assets/templates/gromacs-mdrun-slurm.sh>)

### 参考

- [references/cluster-execution-playbook.md](<modules/hpc-gromacs/references/cluster-execution-playbook.md>)
- [references/ensembles-and-analysis.md](<modules/hpc-gromacs/references/ensembles-and-analysis.md>)
- [references/error-recovery.md](<modules/hpc-gromacs/references/error-recovery.md>)
- [references/file-and-parameter-matrix.md](<modules/hpc-gromacs/references/file-and-parameter-matrix.md>)
- [references/mdp-coupling-and-constraints-matrix.md](<modules/hpc-gromacs/references/mdp-coupling-and-constraints-matrix.md>)
- [references/restarts-and-output-control.md](<modules/hpc-gromacs/references/restarts-and-output-control.md>)
- [references/topology-and-system-building.md](<modules/hpc-gromacs/references/topology-and-system-building.md>)
- [references/workflow-manual.md](<modules/hpc-gromacs/references/workflow-manual.md>)

### 模板

- [assets/templates/em.mdp](<modules/hpc-gromacs/assets/templates/em.mdp>)
- [assets/templates/gromacs-mdrun-slurm.sh](<modules/hpc-gromacs/assets/templates/gromacs-mdrun-slurm.sh>)
- [assets/templates/md_prod.mdp](<modules/hpc-gromacs/assets/templates/md_prod.mdp>)
- [assets/templates/npt.mdp](<modules/hpc-gromacs/assets/templates/npt.mdp>)
- [assets/templates/nvt.mdp](<modules/hpc-gromacs/assets/templates/nvt.mdp>)

## hpc-orchestration

[完整流程](<modules/hpc-orchestration/WORKFLOW.md>)

任务：集群 排队 提交 监控 日志 调度 并行 Slurm PBS LSF

### 工具

- [assets/templates/jupyter-lab-compute.sh](<modules/hpc-orchestration/assets/templates/jupyter-lab-compute.sh>)
- [assets/templates/lsf-basic.sh](<modules/hpc-orchestration/assets/templates/lsf-basic.sh>)
- [assets/templates/pbs-basic.sh](<modules/hpc-orchestration/assets/templates/pbs-basic.sh>)
- [assets/templates/rsync-stage-in.sh](<modules/hpc-orchestration/assets/templates/rsync-stage-in.sh>)
- [assets/templates/slurm-apptainer.sh](<modules/hpc-orchestration/assets/templates/slurm-apptainer.sh>)
- [assets/templates/slurm-array.sh](<modules/hpc-orchestration/assets/templates/slurm-array.sh>)
- [assets/templates/slurm-basic.sh](<modules/hpc-orchestration/assets/templates/slurm-basic.sh>)
- [assets/templates/slurm-packed-single-node.sh](<modules/hpc-orchestration/assets/templates/slurm-packed-single-node.sh>)
- [assets/templates/slurm-perf-report.sh](<modules/hpc-orchestration/assets/templates/slurm-perf-report.sh>)
- [scripts/hpc_job_monitor.py](<modules/hpc-orchestration/scripts/hpc_job_monitor.py>)
- [scripts/hpc_job_submitter.py](<modules/hpc-orchestration/scripts/hpc_job_submitter.py>)
- [scripts/hpc_log_tracker.py](<modules/hpc-orchestration/scripts/hpc_log_tracker.py>)
- [scripts/hpc_slurm_deploy.py](<modules/hpc-orchestration/scripts/hpc_slurm_deploy.py>)

### 参考

- [references/cluster-operations-manual.md](<modules/hpc-orchestration/references/cluster-operations-manual.md>)
- [references/container-workflows.md](<modules/hpc-orchestration/references/container-workflows.md>)
- [references/data-transfer-and-staging.md](<modules/hpc-orchestration/references/data-transfer-and-staging.md>)
- [references/ecosystem-roadmap.md](<modules/hpc-orchestration/references/ecosystem-roadmap.md>)
- [references/environment-and-storage-hygiene.md](<modules/hpc-orchestration/references/environment-and-storage-hygiene.md>)
- [references/error-pattern-dictionary.md](<modules/hpc-orchestration/references/error-pattern-dictionary.md>)
- [references/interactive-debugging-and-profiling.md](<modules/hpc-orchestration/references/interactive-debugging-and-profiling.md>)
- [references/legacy-template.md](<modules/hpc-orchestration/references/legacy-template.md>)
- [references/lifecycle-manual.md](<modules/hpc-orchestration/references/lifecycle-manual.md>)
- [references/public-protocol.md](<modules/hpc-orchestration/references/public-protocol.md>)
- [references/remote-development-and-notebooks.md](<modules/hpc-orchestration/references/remote-development-and-notebooks.md>)
- [references/scheduler-and-parallelism.md](<modules/hpc-orchestration/references/scheduler-and-parallelism.md>)
- [references/slurm-launch-patterns.md](<modules/hpc-orchestration/references/slurm-launch-patterns.md>)
- [references/software-build-and-reproducibility.md](<modules/hpc-orchestration/references/software-build-and-reproducibility.md>)
- [references/tools-and-scripts.md](<modules/hpc-orchestration/references/tools-and-scripts.md>)

### 模板

- [assets/templates/jupyter-lab-compute.sh](<modules/hpc-orchestration/assets/templates/jupyter-lab-compute.sh>)
- [assets/templates/lsf-basic.sh](<modules/hpc-orchestration/assets/templates/lsf-basic.sh>)
- [assets/templates/pbs-basic.sh](<modules/hpc-orchestration/assets/templates/pbs-basic.sh>)
- [assets/templates/rsync-stage-in.sh](<modules/hpc-orchestration/assets/templates/rsync-stage-in.sh>)
- [assets/templates/slurm-apptainer.sh](<modules/hpc-orchestration/assets/templates/slurm-apptainer.sh>)
- [assets/templates/slurm-array.sh](<modules/hpc-orchestration/assets/templates/slurm-array.sh>)
- [assets/templates/slurm-basic.sh](<modules/hpc-orchestration/assets/templates/slurm-basic.sh>)
- [assets/templates/slurm-packed-single-node.sh](<modules/hpc-orchestration/assets/templates/slurm-packed-single-node.sh>)
- [assets/templates/slurm-perf-report.sh](<modules/hpc-orchestration/assets/templates/slurm-perf-report.sh>)
- [assets/templates/ssh-config-compute-proxy.example](<modules/hpc-orchestration/assets/templates/ssh-config-compute-proxy.example>)

## molecular-dynamics

[完整流程](<modules/molecular-dynamics/WORKFLOW.md>)

任务：分子动力学 构象 采样 模拟 轨迹

### 参考

- [references/mdanalysis_analysis.md](<modules/molecular-dynamics/references/mdanalysis_analysis.md>)
- [references/system_preparation.md](<modules/molecular-dynamics/references/system_preparation.md>)

## rdkit-conf

[完整流程](<modules/rdkit-conf/WORKFLOW.md>)

任务：构象 生成三维 初始结构 SMILES 3D ETKDG 力场

### 工具

- [scripts/rdkit_conf_helper.py](<modules/rdkit-conf/scripts/rdkit_conf_helper.py>)
