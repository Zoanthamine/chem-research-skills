# v1.3.1 经验与能力说明版

这一版回答“配置后到底能做什么、能做到哪一步”，并把作者本机的一部分实践经验**脱敏**后并入公开包。

## 新增

- `docs/CAPABILITY-MATRIX.md`：六层能力矩阵——只装包 / +foundation / +spectra / +crystal / +专业软件 / +集群，每项标 `[已跑通]`、`[组件可用]`、`[需外部]`；并给出“迁移目的满足度”对照。
- `docs/DESENSITIZATION.md`：脱敏规则（删了什么、保留什么、如何贡献自己的经验）。
- `skills/huangjt-computational-chemistry/references/`：
  - `practice-lessons.md`：构象/核磁/耦合/TS 的可迁移规则与排错清单（来自真实项目日志，已去样品与数值）
  - `backend-operations.md`：运行时注册表、程序边界、集群/调度坑位、ORCA MPI、种子与构象身份
  - `method-profiles.md`：一套自洽的构象/DFT/NMR/ECD 方法组合示例
- `skills/huangjt-spectral-structure-analysis/references/`：
  - `case-lessons.md`：一次脱氧产物重排鉴定的证据组织与坑位复盘（无样品号、无未发表数值）
  - `environment-tested.json`：数值自检的机器环境记录
- 各技能 `CAPABILITIES.md`、`README.md`、`docs/CATALOG.md` 增加上述入口。
- 同时清掉一处旧示例中的真实构象权重（`postprocess-cli.md`），改为通用占位值。

## 没有做

- 未上传原始谱、结构文件、计算输出、聊天记录、服务器信息或任何凭据；未上传第三方软件/上游技能正文。
- 未重跑科学验收；`CAPABILITY-MATRIX.md` 里明确区分“已跑通 / 组件可用 / 需外部”。
- 公开版仍是精简版：单晶上游模块正文用 `fetch-source crystal` 取，32 个写作可选模块用 `restore-optional` 从 v1.1.0 恢复。

## 升级

```bash
python install.py --check
python install.py --host dsh --replace     # 旧版自动备份
python tools/doctor.py
```