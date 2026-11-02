# 计算化学与核磁计算：完整能力目录

方法、脚本、参考和模板均按任务加载。本目录用于发现能力，完整操作流程在各 WORKFLOW 内；软件未安装时保留知识并按基础迁移说明补齐。

[实操与联动](references/applied-workflows.md) · [基础与迁移](references/foundation-and-migration.md)

## 主技能自带工具

- [backend_inventory.py](scripts/backend_inventory.py) — Inspect configured executable availability without launching software or network.
- [coupling_postprocess.py](scripts/coupling_postprocess.py) — Scale one FC protocol at a time; optional signed, explicit conformer weighting.

## hpc-gaussian

[完整工作流](modules/hpc-gaussian/WORKFLOW.md)

Build, review, debug, and automate Gaussian quantum chemistry workflows. Use when working with Gaussian input files, Link 0 directives, route sections, charge and multiplicity, basis sets, SCF or optimization or frequency jobs, checkpoint handoff, or Gaussian execution and restart issues.

随包脚本 1 项；参考文档 9 项；模板/示例 3 项。

### 脚本

- [assets/templates/gaussian-g16-slurm.sh](modules/hpc-gaussian/assets/templates/gaussian-g16-slurm.sh) — SBATCH --job-name=gaussian_job

### 参考

- [references/checkpoint-restart-and-artifacts.md](modules/hpc-gaussian/references/checkpoint-restart-and-artifacts.md)
- [references/cluster-execution-playbook.md](modules/hpc-gaussian/references/cluster-execution-playbook.md)
- [references/error-pattern-dictionary.md](modules/hpc-gaussian/references/error-pattern-dictionary.md)
- [references/error-recovery.md](modules/hpc-gaussian/references/error-recovery.md)
- [references/geometry-charge-spin.md](modules/hpc-gaussian/references/geometry-charge-spin.md)
- [references/input-and-link0-matrix.md](modules/hpc-gaussian/references/input-and-link0-matrix.md)
- [references/method-basis-and-jobtype.md](modules/hpc-gaussian/references/method-basis-and-jobtype.md)
- [references/scf-opt-freq-and-solvation.md](modules/hpc-gaussian/references/scf-opt-freq-and-solvation.md)
- [references/workflow-manual.md](modules/hpc-gaussian/references/workflow-manual.md)

### 模板与示例

- [assets/templates/gaussian-g16-slurm.sh](modules/hpc-gaussian/assets/templates/gaussian-g16-slurm.sh)
- [assets/templates/opt_freq_water.gjf](modules/hpc-gaussian/assets/templates/opt_freq_water.gjf)
- [assets/templates/sp_water.gjf](modules/hpc-gaussian/assets/templates/sp_water.gjf)

## hpc-gromacs

[完整工作流](modules/hpc-gromacs/WORKFLOW.md)

Build, review, debug, and automate GROMACS molecular simulation workflows. Use when working with GROMACS preprocessing, topology and coordinate files, `.mdp` parameters, energy minimization, equilibration, production MD, analysis commands, or GROMACS runtime errors.

随包脚本 1 项；参考文档 8 项；模板/示例 5 项。

### 脚本

- [assets/templates/gromacs-mdrun-slurm.sh](modules/hpc-gromacs/assets/templates/gromacs-mdrun-slurm.sh) — SBATCH --job-name=gromacs_md

### 参考

- [references/cluster-execution-playbook.md](modules/hpc-gromacs/references/cluster-execution-playbook.md)
- [references/ensembles-and-analysis.md](modules/hpc-gromacs/references/ensembles-and-analysis.md)
- [references/error-recovery.md](modules/hpc-gromacs/references/error-recovery.md)
- [references/file-and-parameter-matrix.md](modules/hpc-gromacs/references/file-and-parameter-matrix.md)
- [references/mdp-coupling-and-constraints-matrix.md](modules/hpc-gromacs/references/mdp-coupling-and-constraints-matrix.md)
- [references/restarts-and-output-control.md](modules/hpc-gromacs/references/restarts-and-output-control.md)
- [references/topology-and-system-building.md](modules/hpc-gromacs/references/topology-and-system-building.md)
- [references/workflow-manual.md](modules/hpc-gromacs/references/workflow-manual.md)

### 模板与示例

- [assets/templates/em.mdp](modules/hpc-gromacs/assets/templates/em.mdp)
- [assets/templates/gromacs-mdrun-slurm.sh](modules/hpc-gromacs/assets/templates/gromacs-mdrun-slurm.sh)
- [assets/templates/md_prod.mdp](modules/hpc-gromacs/assets/templates/md_prod.mdp)
- [assets/templates/npt.mdp](modules/hpc-gromacs/assets/templates/npt.mdp)
- [assets/templates/nvt.mdp](modules/hpc-gromacs/assets/templates/nvt.mdp)

## hpc-orchestration

[完整工作流](modules/hpc-orchestration/WORKFLOW.md)

Coordinate end-to-end HPC execution workflows across scheduler submission, job monitoring, log tracking, self-healing, and post-processing handoff. Use when a task spans Slurm, PBS, LSF, MPI sizing, queue operations, cluster-safe execution, or multi-stage HPC workflow orchestration.

随包脚本 13 项；参考文档 15 项；模板/示例 10 项。

### 脚本

- [assets/templates/jupyter-lab-compute.sh](modules/hpc-orchestration/assets/templates/jupyter-lab-compute.sh) — port="${1:-8888}"
- [assets/templates/lsf-basic.sh](modules/hpc-orchestration/assets/templates/lsf-basic.sh) — BSUB -J hpc_job
- [assets/templates/pbs-basic.sh](modules/hpc-orchestration/assets/templates/pbs-basic.sh) — PBS -N hpc_job
- [assets/templates/rsync-stage-in.sh](modules/hpc-orchestration/assets/templates/rsync-stage-in.sh) — src_dir="${1:-./case/}"
- [assets/templates/slurm-apptainer.sh](modules/hpc-orchestration/assets/templates/slurm-apptainer.sh) — SBATCH --job-name=apptainer_job
- [assets/templates/slurm-array.sh](modules/hpc-orchestration/assets/templates/slurm-array.sh) — SBATCH --job-name=array_job
- [assets/templates/slurm-basic.sh](modules/hpc-orchestration/assets/templates/slurm-basic.sh) — SBATCH --job-name=hpc_job
- [assets/templates/slurm-packed-single-node.sh](modules/hpc-orchestration/assets/templates/slurm-packed-single-node.sh) — SBATCH --job-name=packed_jobs
- [assets/templates/slurm-perf-report.sh](modules/hpc-orchestration/assets/templates/slurm-perf-report.sh) — SBATCH --job-name=perf_report
- [scripts/hpc_job_monitor.py](modules/hpc-orchestration/scripts/hpc_job_monitor.py) — HPC Job Monitor Tool for AI Agents. Monitors the status of a submitted job across Slurm, PBS/Torque, or LSF schedulers. Returns standardized states: PENDING, RUNNING, COMPLETED, FA
- [scripts/hpc_job_submitter.py](modules/hpc-orchestration/scripts/hpc_job_submitter.py) — HPC Job Submitter Tool for AI Agents. Generates batch scripts for Slurm, PBS/Torque, or LSF schedulers, and optionally submits them to the queue.
- [scripts/hpc_log_tracker.py](modules/hpc-orchestration/scripts/hpc_log_tracker.py) — def tail_file(filepath, wait_timeout):
- [scripts/hpc_slurm_deploy.py](modules/hpc-orchestration/scripts/hpc_slurm_deploy.py) — def generate_slurm_script(args):

### 参考

- [references/cluster-operations-manual.md](modules/hpc-orchestration/references/cluster-operations-manual.md)
- [references/container-workflows.md](modules/hpc-orchestration/references/container-workflows.md)
- [references/data-transfer-and-staging.md](modules/hpc-orchestration/references/data-transfer-and-staging.md)
- [references/ecosystem-roadmap.md](modules/hpc-orchestration/references/ecosystem-roadmap.md)
- [references/environment-and-storage-hygiene.md](modules/hpc-orchestration/references/environment-and-storage-hygiene.md)
- [references/error-pattern-dictionary.md](modules/hpc-orchestration/references/error-pattern-dictionary.md)
- [references/interactive-debugging-and-profiling.md](modules/hpc-orchestration/references/interactive-debugging-and-profiling.md)
- [references/legacy-template.md](modules/hpc-orchestration/references/legacy-template.md)
- [references/lifecycle-manual.md](modules/hpc-orchestration/references/lifecycle-manual.md)
- [references/public-protocol.md](modules/hpc-orchestration/references/public-protocol.md)
- [references/remote-development-and-notebooks.md](modules/hpc-orchestration/references/remote-development-and-notebooks.md)
- [references/scheduler-and-parallelism.md](modules/hpc-orchestration/references/scheduler-and-parallelism.md)
- [references/slurm-launch-patterns.md](modules/hpc-orchestration/references/slurm-launch-patterns.md)
- [references/software-build-and-reproducibility.md](modules/hpc-orchestration/references/software-build-and-reproducibility.md)
- [references/tools-and-scripts.md](modules/hpc-orchestration/references/tools-and-scripts.md)

### 模板与示例

- [assets/templates/jupyter-lab-compute.sh](modules/hpc-orchestration/assets/templates/jupyter-lab-compute.sh)
- [assets/templates/lsf-basic.sh](modules/hpc-orchestration/assets/templates/lsf-basic.sh)
- [assets/templates/pbs-basic.sh](modules/hpc-orchestration/assets/templates/pbs-basic.sh)
- [assets/templates/rsync-stage-in.sh](modules/hpc-orchestration/assets/templates/rsync-stage-in.sh)
- [assets/templates/slurm-apptainer.sh](modules/hpc-orchestration/assets/templates/slurm-apptainer.sh)
- [assets/templates/slurm-array.sh](modules/hpc-orchestration/assets/templates/slurm-array.sh)
- [assets/templates/slurm-basic.sh](modules/hpc-orchestration/assets/templates/slurm-basic.sh)
- [assets/templates/slurm-packed-single-node.sh](modules/hpc-orchestration/assets/templates/slurm-packed-single-node.sh)
- [assets/templates/slurm-perf-report.sh](modules/hpc-orchestration/assets/templates/slurm-perf-report.sh)
- [assets/templates/ssh-config-compute-proxy.example](modules/hpc-orchestration/assets/templates/ssh-config-compute-proxy.example)

## molecular-dynamics

[完整工作流](modules/molecular-dynamics/WORKFLOW.md)

Runs and analyzes molecular dynamics simulations with OpenMM and MDAnalysis. Sets up protein/small molecule systems, defines force fields, runs energy minimization and production MD, and analyzes trajectories (RMSD, RMSF, contact maps, free energy surfaces). For structural biology, drug binding, and biophysics.

随包脚本 0 项；参考文档 2 项；模板/示例 0 项。

### 参考

- [references/mdanalysis_analysis.md](modules/molecular-dynamics/references/mdanalysis_analysis.md)
- [references/system_preparation.md](modules/molecular-dynamics/references/system_preparation.md)

## rdkit-conf

[完整工作流](modules/rdkit-conf/WORKFLOW.md)

A standardized CLI wrapper for RDKit 3D/2D conformer generation that samples multiple conformers per molecule (ETKDGv3, default 10), optimizes each with a force field (MMFF94s/UFF), keeps the lowest-energy conformer, automatically falls back to 2D layout on total embedding failure with a printed warning, and writes results to SDF or XYZ format. USE WHEN you need to generate 3D (or 2D fallback) molecular geometries from SMILES datasets (.csv/.smi) for downstream tasks such as docking, visualization, or 3D-descriptor computation.


随包脚本 1 项；参考文档 0 项；模板/示例 0 项。

### 脚本

- [scripts/rdkit_conf_helper.py](modules/rdkit-conf/scripts/rdkit_conf_helper.py) — rdkit_conf_helper.py A minimal CLI wrapper for RDKit conformer generation: - conf : Generate 3D conformers (with 2D fallback) and write to SDF or XYZ Design goal: Work with `uv run
