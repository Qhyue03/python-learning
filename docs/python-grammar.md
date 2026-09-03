# Python 语法最小集（读代码视角）

> 用途：做练习时像查字典一样翻。每条 = 可运行的代码 + 输出 + 一句话解释。
> 学习方法：**先盖住输出猜结果，再运行验证**——猜错的地方就是你的盲区，值得停下来想。
> 所有代码都可在 VS Code 里新建临时文件直接跑。

## 1. 变量：不用声明类型，直接赋

```python
x = 5              # 整数 int
y = 2.5            # 小数 float
s = "hello"        # 字符串 str
ok = True          # 布尔 bool（注意大写开头）
print(x, y, s, ok) # 输出: 5 2.5 hello True
```

一句话：变量就是个贴了名字的盒子，随时可以换内容。`type(x)` 可以查看类型。

## 2. f-string：往文字里嵌变量（本月最高频）

```python
name = "邱"
n = 3
print(f"我是{name}，第{n}天")     # 输出: 我是邱，第3天
print(f"[{n:^10}]")                # 输出: [    3     ]  ^10 = 10格内居中
print(f"[{n:>10}]")                # 输出: [         3]  >10 = 右对齐
print(f"{2.718:.1f}")              # 输出: 2.7          .1f = 保留1位小数
```

## 3. 字符串：能加、能乘、能切

```python
s = "ab" + "cd"       # 拼接 → "abcd"
bar = "-" * 8          # 重复 → "--------"
w = "python"
print(w[0], w[-1])     # 输出: p n    （下标从0开始，-1是最后一个）
print(w[0:3])          # 输出: pyth   （含头不含尾）
print(len(w))          # 输出: 6      （长度）
```

## 4. 列表：一串值的有序盒子

```python
nums = [10, 20, 30]    # 创建
nums.append(40)        # 末尾追加 → [10, 20, 30, 40]
print(nums[0])         # 输出: 10     （第一个）
print(nums[-1])        # 输出: 40     （最后一个）
print(len(nums))       # 输出: 4
print(nums[1:3])       # 输出: [20, 30]（切片，含头不含尾）
```

## 5. for + range：重复指定次数（对照 C++ 的 for i）

```python
for i in range(3):         # 0, 1, 2   （从0开始，含头不含尾）
    print(i, end=" ")      # 输出: 0 1 2
# range(1, 6)    → 1 2 3 4 5
# range(10, 0, -1) → 10 9 8 ... 1   （第三个参数是步长，-1是倒着走）
# range(0, 21, 2) → 0 2 4 ... 20    （步长2，全是偶数）
```

`end=" "` 让 print 不换行，用空格代替。

## 6. for 遍历列表：逐个拿出元素

```python
fruits = ["a", "b", "c"]
for f in fruits:           # f 依次是 "a", "b", "c"
    print(f)
# 输出三行: a / b / c
```

## 7. 累加器模式（C++ 课堂最经典，必背）

```python
total = 0
for i in range(1, 101):    # 1 到 100
    total = total + i      # 也可写 total += i
print(total)               # 输出: 5050
```

模式：**循环外建盒子 → 循环内往盒子里加东西 → 循环外用**。计数器同理（`count += 1`）。

## 8. if / elif / else

```python
x = 7
if x > 10:
    print("大")
elif x > 5:
    print("中")            # 输出这个：中（从上往下第一个命中的分支）
else:
    print("小")
```

注意：相等判断是 `==`（一个=是赋值）；并且/或/非是 `and` / `or` / `not`。

## 9. 列表套列表：表格 / 矩阵的雏形

```python
m = [[1, 2], [3, 4], [5, 6]]   # 3行2列
print(m[0])        # 输出: [1, 2]     （第0行，整行）
print(m[0][1])     # 输出: 2          （第0行第1个）
print(len(m))      # 输出: 3          （行数）
for row in m:      # row 依次是 [1,2] / [3,4] / [5,6]
    print(row)
```

## 10. 函数：把一段逻辑装盒子

```python
def add(a, b):         # a、b 是参数（占位）
    return a + b       # return 把结果交回去

r = add(3, 4)
print(r)               # 输出: 7

def greet(name, punc="!"):          # =后面的叫默认参数，可不传
    return f"hi {name}{punc}"

print(greet("py"))                  # 输出: hi py!
print(greet("py", punc="?"))        # 输出: hi py?
```

`print` 和 `return` 的区别：return 是把值**交还给调用处**；print 只是显示。函数不写 return 等于返回 None。

## 11. 读报错：报错的最后一行是答案

| 报错最后一行 | 意思 | 常见原因 |
|---|---|---|
| `NameError: name 'x' is not defined` | 变量不存在 | 拼错名字、用了没赋值的变量 |
| `IndexError: list index out of range` | 下标越界 | `nums[5]` 但列表只有3个（下标最大是2！） |
| `TypeError: can only concatenate str...` | 类型不匹配 | 数字和字符串相加，该用 `str(x)` 或 f-string |
| `IndentationError` | 缩进错误 | 冒号后面忘了缩进，或缩进忽大忽小 |
| `SyntaxError` | 语法错误 | 少了冒号、括号没配对（看报错指的行号附近） |

**读报错三步**：看最后一行（什么错）→ 看它上面指的 `File "xxx", line N`（哪一行）→ 去那行附近找。

## 12. 猜输出训练（现在就做，答案在文末）

```python
# 片段1
s = 0
for i in range(1, 5):
    s += i
print(s)

# 片段2
w = "yanghui"
print(w[0:4], len(w))

# 片段3
m = [[1], [1, 1], [1, 2, 1]]
print(m[2])
print(m[2][1])
print(m[-1][-1])

# 片段4
def double(x):
    return x * 2
print(double(double(3)))
```

<details>
<summary>答案（先猜完再展开）</summary>

1. `10`（1+2+3+4）
2. `yang 7`
3. `[1, 2, 1]`、`2`、`1`（-1 是最后一个的第-1个，即 1）
4. `12`（3→6→12，函数可以套自己）

</details>
