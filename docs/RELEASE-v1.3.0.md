# v1.3.0 新手上路版

这一版不改科学方法，改的是**别人拿到这份包之后能不能顺利配置和使用**。

## 新增

- `tools/doctor.py`：只读体检——仓库完整性、宿主（DSH/Codex）与安装状态、Python 依赖 profile、外部专业软件（DIALS/Gaussian/ORCA/SHELX/GROMACS/xTB/ThermoRawFileParser…），最后给出下一步命令。`--json` 可给代理/CI 用。
- `tools/inventory.py` + `docs/INVENTORY.md` / `inventory.csv` / `inventory.html`：逐文件用途索引（入口/工具/函数库/测试/参考/资源/许可/上游框架），可搜索、可筛选；CI 防止过期。
- `tools/manifest.py`：重新生成或校验 `MANIFEST.json`，把“账本与工作树不一致”从人工检查变成命令。
- `docs/QUICKSTART.md`：5 分钟上手（校验 → 试装 → 安装 → 自检 → 配基础后端 → 第一次任务 → 更新回滚）。
- `docs/TROUBLESHOOTING.md`：按症状查的排错表（校验失败、冲突拒绝、技能不出现、依赖、专业软件、数据格式）。
- `docs/WORKFLOWS.md`：六条真实工作流（输入 → 阶段 → 需要的软件 → 已验证/未验证边界）。
- `docs/MAINTAINERS.md`：需求来源、红线、发布流程、CI 项、版本策略。
- `examples/quickstart_smoke.py`：不装任何专业软件就能跑的离线冒烟。
- `install.sh`：macOS/Linux 入口（与两个 `.cmd` 对应）。
- `.github/workflows/release.yml`：打 tag 时自动生成源码 zip + `SHA256SUMS.txt` 并挂到 Release。

## 改进

- `install.py`：新增 `--dry-run`（只出计划）、`--host auto`（检测已存在宿主）、`--smoke`（装后自检）、`--json`、人类可读的安装总结与下一步提示；冲突与 `--replace` 行为不变（先备份）。
- `check.yml`：恢复完整检查（账本、索引、单元测试、单晶回归、谱学自检、离线冒烟、doctor），Python 升到 3.12；不再依赖 `[skip ci]` 的人工判断。
- `README.md`：改为“三步上手 + 你会得到什么 + 文档地图”。
- `docs/CATALOG.md`：加入新手上路、工作流、逐文件索引入口。

## 没有做什么

- 未重跑科学验收：单晶全链、任意分子的构象/核磁、真实样品结构鉴定都没有在这次发布前重新验证。已有的组件级记录见 `docs/CORE_ACCEPTANCE.md`。
- 未新增专业软件或模型，未改技能的方法内容；32 个可选模块仍未随包分发（索引与恢复方式不变）。
- v1.2.0 的 tag 不动。

## 升级方式

```bash
python install.py --check
python install.py --host dsh --replace    # 旧版自动备份到 chemistry-skill-backups/
python tools/doctor.py
```

只改全局规则不需要重装：安装器会原地替换受管块并保持你 `AGENTS.md` 的其余内容。