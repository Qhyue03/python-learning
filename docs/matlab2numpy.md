# MATLAB ↔ NumPy 对照速查表

给 MATLAB 背景的自己看的。`import numpy as np` 后对照使用。

## 最大的一页：思维方式

| | MATLAB | NumPy |
|---|---|---|
| 万物皆矩阵 | 默认二维矩阵 | 默认一维数组（向量不是 n×1 矩阵！） |
| 索引从 1 开始 | `A(1)` | `A[0]` |
| 切片含两端 | `A(2:5)` 取 4 个 | `A[1:5]` 含头不含尾，取 4 个 |
| 按列存储 | 列主序 | **行主序**（reshape 结果不同，见下） |
| 复数转置 | `A'` 是共轭转置 | `A.T` 是纯转置；共轭转置是 `A.conj().T` |
| 循环慢所以向量化 | `.*/.^` 逐元素 | `* ** /` 本来就逐元素；矩阵乘法反而要 `@` |

## 基础操作

| 用途 | MATLAB | NumPy |
|---|---|---|
| 行向量 | `[1 2 3]` | `np.array([1, 2, 3])` |
| 等距向量 | `linspace(a,b,n)` | `np.linspace(a, b, n)` |
| 零矩阵 | `zeros(3,4)` | `np.zeros((3, 4))` 注意双层括号 |
| 单位阵 | `eye(3)` | `np.eye(3)` |
| 随机数 | `rand(3,4)` | `rng = np.random.default_rng(0); rng.random((3,4))` |
| 尺寸 | `size(A)` | `A.shape`（属性不是函数） |
| 元素数 | `numel(A)` | `A.size` |
| 改形 | `reshape(A, m, n)` | `A.reshape(m, n)`（列主序陷阱！MATLAB 按列取数，NumPy 按行。要对齐 MATLAB：`A.reshape(m, n, order='F')`） |
| 拼接 | `[A; B]` / `[A, B]` | `np.vstack((A,B))` / `np.hstack((A,B))` |
| 查找 | `find(x > 0)` | `np.nonzero(x > 0)[0]` |
| 逐元素函数 | `sin(A)` 天然逐元素 | `np.sin(A)` 天然逐元素 |

## 矩阵运算

| 用途 | MATLAB | NumPy |
|---|---|---|
| 矩阵乘法 | `A * B` | `A @ B` |
| 逐元素乘 | `A .* B` | `A * B` |
| 逐元素幂 | `A .^ 2` | `A ** 2` |
| 求解 Ax=b | `A \ b` | `np.linalg.solve(A, b)` |
| 最小二乘 | `A \ b`（超定） | `np.linalg.lstsq(A, b)` |
| 逆 / 秩 | `inv(A)` / `rank(A)` | `np.linalg.inv(A)` / `np.linalg.matrix_rank(A)` |
| SVD | `[U,S,V]=svd(A)` | `U, S, Vt = np.linalg.svd(A)`（注意返回 V 的转置） |
| FFT | `fft2(A)` | `np.fft.fft2(A)`；居中显示用 `np.fft.fftshift` |

## 网格与可视化（做相位图天天用）

| 用途 | MATLAB | NumPy / Matplotlib |
|---|---|---|
| 网格 | `[X,Y]=meshgrid(x,y)` | `X, Y = np.meshgrid(x, y)`（默认 indexing='xy' 与 MATLAB 一致） |
| 画强度图 | `imagesc(I); colorbar` | `plt.imshow(I, cmap='gray'); plt.colorbar()` |
| 3D 表面 | `surf(X,Y,Z)` | `ax = plt.figure().add_subplot(projection='3d'); ax.plot_surface(X, Y, Z, cmap='viridis')` |
| 相位卷绕显示 | `angle(W)` 后 imagesc | `np.angle(W)`（结果就在 [-π, π]） |
| 保存图 | `saveas(gcf,'a.png')` | `plt.savefig('a.png', dpi=150)` |

## 语言层

| | MATLAB | Python |
|---|---|---|
| 注释 | `%` | `#` |
| 块结束 | `end` | 缩进（4 空格，不许 tab 空格混用） |
| 函数 | `function y = f(x)` 单独 .m 文件 | `def f(x):`，任意文件任意位置 |
| 多返回值 | `[a, b] = f(x)` | `a, b = f(x)` |
| 文档 | 函数上方 `%` 注释 | 函数体首行三引号 docstring |
| i 从 1 到 10 | `for i = 1:10` | `for i in range(1, 11)` |
| 复用代码 | addpath | `import mylib`（同目录或包） |

## 常见坑（MATLAB 用户高发）

1. `A.reshape` 的行列主序差异——迁移老代码时结果形状对但数值错位，先怀疑这里。
2. 向量 `(n,)` 和 `(n,1)` 不是一回事：`np.dot` 行为不同。用 `v[:, None]` 或 `v.reshape(-1, 1)` 升维。
3. 整数除法 `5/2`：MATLAB 得 2.5；Python 的 `int/int` 也得 2.5，但 `5//2` 得 2（别乱用 `//`）。
4. 赋值是引用：`B = A` 后改 `B` 会动 `A`，要副本用 `B = A.copy()`。
5. 布尔索引赋值 `A[A > 1] = 0` 是合法且高效的（对应 MATLAB 的逻辑索引）。
