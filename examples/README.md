# 示例

这些示例只用标准库和随包脚本，不需要安装任何专业软件。

## `quickstart_smoke.py`

装之前/装之后都能跑的离线冒烟：

```bash
python examples/quickstart_smoke.py
python examples/quickstart_smoke.py --installed-skills ~/.dsh/skills
```

它检查：包完整性（MANIFEST）、六个技能入口、模块索引查询、结构 CLI 帮助；有 `--installed-skills` 时再查一次已安装目录。

## 想看具体用法

- 第一次配置：`docs/QUICKSTART.md`
- 真实工作流与需要的软件：`docs/WORKFLOWS.md`
- 每个文件是什么：`docs/INVENTORY.md`（或在浏览器打开 `docs/inventory.html` 搜索）
- 出错怎么办：`docs/TROUBLESHOOTING.md`