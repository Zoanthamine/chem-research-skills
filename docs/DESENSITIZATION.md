# 本地经验脱敏说明

v1.3.1 把作者本机的一部分实践经验和资料**脱敏后**并入公开包。这份文档说明加了什么、去掉了什么、你怎么贡献自己的经验。

## 新增了什么

| 文件 | 内容 | 来源 |
|---|---|---|
| `skills/huangjt-computational-chemistry/references/practice-lessons.md` | 自由基重排体系的构象/核磁/耦合/TS 可迁移规则与排错清单 | 一次真实项目的日志与纠正记录 |
| `skills/huangjt-computational-chemistry/references/backend-operations.md` | 运行时注册表、程序边界、集群与调度坑位、ORCA MPI/种子/构象身份 | 本机 + 集群配置与故障记录 |
| `skills/huangjt-computational-chemistry/references/method-profiles.md` | 一套自洽的构象/DFT/NMR/ECD 方法组合示例 | 课题组实际方法档 |
| `skills/huangjt-spectral-structure-analysis/references/case-lessons.md` | Barton 脱氧产物重排鉴定的证据组织与坑位复盘 | 一次真实结构鉴定项目 |
| `skills/huangjt-spectral-structure-analysis/references/environment-tested.json` | 数值自检的机器环境记录（说明“跑通”的含义） | 作者机器 |
| `docs/CAPABILITY-MATRIX.md` | 配置到每一步能做什么、缺什么 | 由包内能力盘点得出 |

## 脱敏规则

删除或替换：

- 主机名、IP、端口、账号、SSH 密钥路径、集群绝对路径、本地盘符；
- 项目代号、样品编号、文件名、构象 ID 的原始命名；
- 未发表的精确位移、耦合常数、精确质量、构象权重、覆盖率数值；
- 任何个人姓名、单位、联系方式、聊天记录原文。

保留（可迁移且不含隐私）：

- 方法、基组、泛函、溶剂模型、标度常数（均为公开文献值）；
- 软件行为、命令风格、失败模式与判断规则；
- “已验证/未验证”的边界和交付要求。

## 为什么不直接上传原始资料

- 原始谱、结构文件、计算输出属于未发表科研数据，不能进公开仓库；
- 第三方软件、模型、上游技能包有各自许可，只保留来源与获取方式（见 `SOURCE-LICENSES.json`、`THIRD_PARTY.md` 与 `catalog/`）；
- 作者的机器路径与凭据不具备通用性，且会泄露环境信息。

## 怎么贡献你自己的经验

1. 写进对应技能的 `references/`，一个主题一个文件，开头写“来源与适用范围”。
2. 结构建议：现象/输入 → 判断规则 → 证据 → 反例/边界 → 关联文件。
3. 不写：样品编号、未发表数值、路径、账号、第三方原文大段复制。
4. 改完运行：

```bash
python tools/manifest.py --write
python tools/inventory.py --write
python install.py --check && python tools/manifest.py --check && python tools/inventory.py --check
```

5. 提交 PR 时在描述里写清“脱敏方式”和“适用范围”。

## 许可

新增文字为作者原创，随本库以 MIT 发布；引用文献只给 DOI/出处，不复制原文。`upstream-provenance.json` 记录第三方来源与许可，随包保留。