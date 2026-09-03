row = []
for j in range(0, 4, 1):
    nums = []
    for i in range(0, j + 1):
        val = 1
        nums.append(val)
    row.append(nums)
print(row)
for r in row:
    print(r)
