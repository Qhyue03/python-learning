# 9 月大作业：四步相移 + 相位展开（Python + NumPy 复刻）

把自己的 MATLAB 代码翻译过来。周 4（9/22–9/30）正式开工，第 3 周 ex05 已生成过输入条纹。

## 目标

1. **仿真部分**：生成四步相移条纹（理想 + 含噪两档），或直接用实验室真实图
2. **求包裹相位**：φ_wrapped = atan2(I1 - I3, I2 - I4)，结果卷绕在 [-π, π]
3. **质量图**：调制度 / 梯度差分质量图任选一种
4. **解包裹**：路径法（质量图引导 flooding）或简单 flood fill；先用小尺寸（64×64）调通再放大
5. **验收**：与 MATLAB 结果逐点对比，`np.max(np.abs(phi_py - phi_ml)) < 1e-10`；平坦相位场景解包裹无 2π 跳变

## 工程要求

```
phase-project/
  main.py          # 入口：argparse 选数据源和参数
  fringe.py        # 条纹生成
  wrapped.py       # 包裹相位
  quality.py       # 质量图
  unwrap.py        # 解包裹
  visualize.py     # 出图
  test_smoke.py    # 冒烟测试：小尺寸仿真全流程跑通（assert 误差）
```

- 每个模块一个职责，函数有 docstring
- 出图四联：条纹 / 包裹相位 / 质量图 / 解包裹 3D 表面
- README 记录：MATLAB → Python 踩的坑列表（这本身就是面试素材）

## 提醒

- 上传 GitHub 前做一次无 AI 复写（红线）
- 10 月起这份代码就是 HDR 项目的地基，值得写干净
