# DDCA 自学进度表

面向 ETH Zurich Digital Design and Computer Architecture（DDCA）的自学进度模板。以课件为主线，用理论习题和实验验证理解。

## 包含什么

- 36 个理论课件单元，保留官方 L 编号和 a/b 拆分。
- 6 套 2025 年 Homework，题目与答案分开链接。
- 10 次 2026 年 Lab：Lab 1–9，其中 Lab 8 分为 8.1、8.2。
- 20 个选学解题单元：D1–D13、L27–L33。
- 两张表的字段、关联、公式、视图与仪表盘搭建说明。

主线合计 52 个任务。完成率按理论课、Homework 和 Lab 分别统计，选学资源不计入分母。

资料核对日期：2026-10-19。当时 2026 Homework 页面为空，因此采用完整的 2025 年版本。课程链接和内容以官方页面为准。

## 文件

| 文件 | 用途 |
| --- | --- |
| `data/tasks.csv` | 可导入 Notion 或其他表格工具的 72 项任务清单 |
| `data/study-log.csv` | 只有表头的空白学习日志 |
| `data/tasks.json` | 完整任务数据、验收提示、资料链接和按编号表达的关联 |
| `schema.json` | 与个人工作区无关的字段、公式、关联和视图定义 |
| `docs/notion-setup.md` | 在 Notion 中恢复表结构与统计的操作说明 |
| `docs/build-prompt.md` | 可交给有数据库写入能力的 Agent 的搭建提示词 |
| `scripts/export_csv.py` | 修改 JSON 后重新生成 CSV，Python 标准库即可运行 |

## 使用方式

1. 将 `data/tasks.csv` 导入为“学习任务”，将 `data/study-log.csv` 用作“学习记录”的空白结构。
2. 按 [Notion 搭建说明](docs/notion-setup.md) 设置字段类型、双向关联、公式、汇总和视图。若工具不接受只有表头的 CSV，手动创建空白日志表。
3. 每次学习后新增真实日志，更新对应任务的状态与掌握程度。

CSV 负责迁移数据，不会自动恢复 Notion 的关联、公式、视图和图表。任务间关系以官方编号保存，需要在新工作区中重新连接。可以把搭建提示词、任务 JSON 与 schema 一起交给支持 Notion 写入的 Agent 完成恢复。

本仓库提供初始模板，不会与任何人的 Notion 页面自动同步。

## 更新任务数据

编辑 `data/tasks.json` 后运行：

```powershell
python scripts/export_csv.py
```

每个任务使用稳定的 `code`；`prereq` 为自学建议的必要基础，`related` 为相关学习内容，二者都引用其他任务的 `code`。不要把个人 Notion 页面 ID 写入模板。

## 学习约定

- 课件为主，录像按需补充，不要求完整观看。
- Homework 先独立尝试，再查看答案并订正。
- Lab 分开记录“仿真通过”和“上板通过”；仿真通过不代表完成真实外设演示。
- Lab 8 为给定框架下的单周期 MIPS 系统集成，Lab 9 扩展指令并分析性能；不把流水线 CPU 实现写成官方实验要求。
- 不预填学习日期、学习时长、完成进度或复习计划。
- 任务完成率不代表知识掌握率。

## 官方资料

- [2026 课件与视频](https://safari.ethz.ch/ddca/spring2026/doku.php?id=schedule)
- [2026 Labs](https://safari.ethz.ch/ddca/spring2026/doku.php?id=labs)
- [2025 Homework 与答案](https://safari.ethz.ch/ddca/spring2025/doku.php?do=show&id=homeworks)
- [2026 阅读资料](https://safari.ethz.ch/ddca/spring2026/doku.php?do=show&id=readings)
- [历年考试](https://safari.ethz.ch/ddca/spring2026/doku.php?do=show&id=exams)

课程由 Onur Mutlu 等教师及 SAFARI 教学团队提供，本项目是独立的自学辅助模板。

## 许可

本项目原创脚本、模板设计和使用说明采用 MIT License，见 [LICENSE](LICENSE)。课程名称、课件、题目、实验材料及链接目标内容归各自权利人所有，不因本项目的 MIT License 而重新授权。本仓库只引用官方资料链接，不收录课件或实验附件。
