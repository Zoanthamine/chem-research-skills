# 维护者手册：需求、发布流程与红线

这份文档记录“为什么长这样”和“改动怎么发布”，供后续维护者（人或代理）接手。  
它不替代 [CORE_ACCEPTANCE.md](CORE_ACCEPTANCE.md) 的科学边界说明。

## 需求来源

以下要求来自作者的 Codex 会话记录与交接文档（2026-11-01 ~ 11-02），按原意归纳：

| # | 要求 | 实现方式 |
|---|---|---|
| 1 | 四个化学核心各自完整，不能合并成一个，也不能只剩短路由 | 六个 `SKILL.md` 独立入口；内部模块只注册 `WORKFLOW.md`，不再注册平级技能 |
| 2 | 两个学术技能提供文献证据与表达支持 | `huangjt-academic-research` / `huangjt-academic-writing`，写作用 7 个默认模块 |
| 3 | 去重、收敛入口时保留知识、方法、脚本和原件；未随包内容要有用途、来源和恢复方式 | `catalog/`（47 模块 + 32 可选 + 252 归档）、`workbench.py search/restore-optional`、`references/absorbed-modules.md` |
| 4 | 自然语言能触发；关键词要具体，别让“分析/计算”抢无关任务 | `routing/global-defaults.md` 六行任务→技能映射；`doctor` 验证规则块只出现一次 |
| 5 | 新电脑先配结构识别、绘制、格式转换等基础能力；开源自动配，授权软件另说，集群可选 | `workbench.py` 六个 profile；`docs/QUICKSTART.md`；`docs/WORKFLOWS.md` 软件矩阵 |
| 6 | 别人也要能用，最好有类似体验；一句话就能在别人电脑配置 | `install.py`（`--dry-run/--auto/--smoke`）、`tools/doctor.py`、`docs/QUICKSTART.md`、`examples/quickstart_smoke.py` |
| 7 | 兼容 Codex 与 DeepSeek Harness | 安装器双宿主；`docs/COMPATIBILITY.md`；同一份技能目录可被两端复用 |
| 8 | 不能因为版权删除脚本；软件可以自己装 | 脚本随包，程序/许可不随包；`LICENSES/` + `SOURCE-LICENSES.json` |
| 9 | 目录要能解释每个文件干什么 | `tools/inventory.py` → `docs/INVENTORY.md`、`inventory.csv`、`inventory.html`（CI 防过期） |
| 10 | 发布前先打包上传，跳过完整回归（作者明确要求） | 发布说明如实写“未追加完整验证”，CI 只跑能跑的部分 |

## 红线

1. **不上传私人内容**：样品数据、原始谱、聊天记录、账号密钥、本机路径配置、商业程序安装包。
2. **四核心不合并**：可以加模块、加参考，不能把单晶/计算/解谱/有机压成一个“化学技能”。
3. **不静默删内容**：移除的模块必须留下索引、来源和恢复路径（`catalog/` + `workbench.py restore-optional`）。
4. **不夸大验证**：区分“文件完整”“入口可加载”“组件跑通”“科学结论成立”，`CORE_ACCEPTANCE.md` 写清楚。
5. **不改写历史版本**：已发布的 tag 不动；修正走新版本。
6. **不把脚本和软件授权混为一谈**：包装是方法+脚本+模板，不是软件分发。

## 发布流程

```bash
# 1. 从 main 拉分支
git switch -c feat/<主题>

# 2. 改内容（技能内容、文档、工具）

# 3. 重新生成账本与索引
python tools/manifest.py --write
python tools/inventory.py --write

# 4. 全量检查（与 CI 相同）
python install.py --check
python tools/manifest.py --check
python tools/inventory.py --check
python -m unittest discover -s tests
python tools/doctor.py --json
python install.py --host dsh --target /tmp/chem-install --no-defaults --smoke   # 临时目录试装

# 5. 提 PR（说明改了什么、为什么、验证到哪一步）

# 6. 合并后打 tag，Release 工作流自动生成源码 zip + SHA256SUMS 并挂到 Release
git tag vX.Y.Z && git push origin vX.Y.Z
```

`VERSION` 与 tag 保持一致；`release.yml` 在 tag 推送时构建 `chem-research-skills-<tag>.zip` 和校验和，并挂到 Release。

## CI 检查项

`.github/workflows/check.yml` 在 Ubuntu 与 Windows 上执行：

1. `install.py --check`（2704 文件账本）
2. `tools/manifest.py --check`（账本是否跟随工作树）
3. `tools/inventory.py --check`（逐文件索引是否过期）
4. `python -m unittest discover -s tests`（安装器、迁移、谱读取、文本输出、工具）
5. 单晶辅助脚本的离线回归测试
6. 谱学 `evidence_cli.py selftest`
7. `doctor.py --json`（只读自检，不因缺少专业软件失败）

## 版本策略

- **PATCH**（1.3.x）：文档、索引、错误信息、兼容性修复。
- **MINOR**（1.x.0）：新增工具/模块/profile，不破坏既有安装与 MANIFEST 语义。
- **MAJOR**（2.0.0）：技能入口或安装布局变更，需要迁移说明。

每次发布在 `docs/RELEASE-<tag>.md` 写：改了什么、没验证什么、如何升级。

## 已知边界与待办

- v1.2.0 的最终提交带 `[skip ci]`，最终树未过 CI；v1.3.0 恢复了完整检查。
- 单晶上游模块 `solve-single-crystal` 的完整正文需 `workbench.py fetch-source crystal` 获取；包内只保留指针与四个知识章节。
- 32 个写作/统计/图形模块只保留索引，正文从 v1.1.0 固定版本恢复。
- ARS 上游框架约 1470 个文件随包分发，但未逐个审查实现；索引里按包归组。
- 自动分类索引可能把个别上游文件标成通用类型，发现后改 `tools/inventory.py` 规则并重新生成。
- 远程/集群、商业软件授权、大规模模型不属于本库范围。
