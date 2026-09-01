# Python 学习 · 2026年9月（阶段1）

MATLAB 熟手 → Python + NumPy 熟手。为 10 月 PyTorch + HDR 相位展开项目打地基。

## 每日节奏（19:30–21:30）

- 前 40 分钟：学新概念（读资料 / 改示例）
- 中间 60 分钟：手写当周练习
- 最后 20 分钟：写复盘笔记（记进 `notes/`，哪怕三行）

**AI 红线**：9 月打地基期尽量不用 AI 帮忙 debug——先自己读报错栈、加 print、用断点单步。卡超过 30 分钟再问。

## 本月路线

| 周 | 日期 | 主题 | 产出 |
|---|---|---|---|
| 1 | 9/1–9/7 | 语法基础：变量 / 容器 / 控制流 / 函数 | `exercises/week01/` |
| 2 | 9/8–9/14 | 语法进阶 + 工程化：文件 / 异常 / 模块 / 调试器 / argparse | `exercises/week02/` |
| 3 | 9/15–9/21 | NumPy 核心：ndarray / 广播 / 向量化（对照 MATLAB） | `exercises/week03/` |
| 4 | 9/22–9/30 | 大作业：四步相移 + 相位展开翻译成 Python + NumPy | `phase-project/` |

> ⚠️ 论文一最迟 9 月中旬投出。周 3、周 4 的学习为论文让路，练习可顺延到国庆。

## 环境

统一用 conda 环境跑（Python 3.12 + NumPy 已装）：

```bash
conda activate torch
python exercises/week01/xxx.py
```

VS Code 打开本目录即可；右下角解释器选 `torch` 环境。

## 目录

- `exercises/week01..04/` —— 每周练习清单在该目录 README
- `phase-project/` —— 9 月大作业（周 4 开始）
- `notes/` —— 每日复盘笔记
- `docs/matlab2numpy.md` —— MATLAB ↔ NumPy 对照速查表

## 提交习惯

每天学完提交一次：`git add . && git commit -m "week01 d1: 容器练习"`。
一个月后回看提交历史，就是你的学习轨迹——面试也能讲。
