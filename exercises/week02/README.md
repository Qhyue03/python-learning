# 第 2 周（9/8–9/14）：语法进阶 + 工程化

目标：从"能跑的脚本"到"像样的程序"。本周起每个文件按 `main()` + `if __name__ == "__main__":` 组织。

- [ ] ex01：读 `data.txt`（自己造：每行 `x y` 两列浮点），手写解析，算每列均值/方差（练文件 IO、字符串 split）
- [ ] ex02：在 ex01 数据里故意插几行脏数据（空行、字母），用 try/except 跳过并计数（练异常）
- [ ] ex03：把上周 `my_linspace` 抽成 `mylib.py`，另一个文件 `from mylib import my_linspace` 使用（练模块）
- [ ] ex04：给 ex01 加 `argparse`：`python ex04.py data.txt --column 0`（练命令行参数）
- [ ] ex05：调试器练习——写一个带 bug 的 20 行程序（比如差一错误），用 VS Code 断点单步找到它（练 debugpy，禁止用 print）
- [ ] ex06：用 `pathlib.Path` 重写 ex01 的文件操作（现代写法，替代 os.path）
- [ ] ex07（综合）：把第 1 周的矩阵乘法包成 CLI 工具 `matmul.py a.txt b.txt -o c.txt`，含参数校验和错误提示

## 工程化清单（本周建立的习惯）

- 文件头三件套：`#!/usr/bin/env python` 可省，但 docstring、`main()`、`__main__` 守卫不能省
- VS Code：Ctrl+S 自动格式化（black），保存即规范
- 每天学完 `git commit`，写清楚干了什么
