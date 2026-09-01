# 第 3 周（9/15–9/21）：NumPy 核心

目标：建立向量化思维，彻底切换到"数组编程"。对照 `docs/matlab2numpy.md`。本周注意：论文优先，练习为论文让路。

- [ ] ex01：ndarray 基础——dtype、shape、reshape；做 order='C' vs order='F' 对比实验（对应 MATLAB 列主序）
- [ ] ex02：广播——列向量 `(n,1)` + 行向量 `(1,m)` 生成网格；实现 `X + Y` 和 `sqrt(X**2 + Y**2)`
- [ ] ex03：索引——花式索引取隔行隔列；布尔掩码把 `A[A>0.5]` 置零（替代 MATLAB find）
- [ ] ex04：向量化改写——用 `@` 重写第 1 周 ex07 矩阵乘法，`time.perf_counter` 对比提速倍数
- [ ] ex05（相移先导）：生成 512×512 正弦条纹 `I = a + b*cos(2πfx + φ)`，φ 取 0/π/2/3π/2 四张，`plt.imshow` 灰度显示——**这就是大作业的输入**
- [ ] ex06：对 ex05 条纹做 2D FFT，`fftshift` 后 `log(1+abs)` 显示频谱，找到 +1 级条纹频率位置
- [ ] ex07：随机数——`rng = np.random.default_rng(0)`，给条纹加高斯噪声，算 SNR
- [ ] ex08：`np.linalg.lstsq` 拟合带噪声直线 y=kx+b，画原图散点+拟合线，输出 k、b 与真值误差

## 自查标准

- 写新循环前先想"能不能广播/向量化"
- 能说清 `(n,)`、`(n,1)`、`(1,n)` 的区别和互相转换
- 会用 `A.sum(axis=?)`、`np.mean(axis=?)` 对指定维度归约
