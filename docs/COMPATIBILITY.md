# 宿主与后端

DSH兼容工作依据本机DeepSeek Harness 0.2.1-rc.2的真实FileSystemSkillProvider：六入口均可发现、加载完整正文并允许模型调用，内部WORKFLOW不作为同级技能发现。Codex使用标准SKILL.md、openai.yaml和全局AGENTS.md。实际加载验证不等同于对任意模型、远程服务或实际样品的端到端验收。

本机将DSH的六入口链接到同一份规范目录，避免复制更新漂移；其他用户安装器复制六个完整文件夹。使用共同科学参数和证据规则，执行工具映射到目标宿主。Codex参考：[全局说明](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[技能发现](https://learn.chatgpt.com/docs/build-skills)。

更新与覆盖：默认保留不同内容的现有技能并报错。--replace先备份，安装器不递归删除旧目录。全局默认规则由明确的开始结束标记管理，不覆盖用户其他规则。撤销默认规则时移除该标记段即可；恢复技能时从安装器报告的备份目录比较还原。

Windows克隆建议使用README中的core.longpaths命令，并选择简短的工作目录；发布包已排除上游长路径测试与评测数据。本包运行检查使用自己的安装测试、单晶辅助测试和数值示例，不要求上游维护仓库的全部文件。

单晶命令行工具显式使用UTF-8输出，支持英语Windows及被宿主重定向的中文日志；测试会模拟cp1252管道，避免只在作者中文环境中通过。科学输入与计算结果的文件处理规则保持原样。
