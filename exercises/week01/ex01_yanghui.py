row = []
for i in range(10):
    nums = []
    for j in range(0, i + 1):
        val = 1
        nums.append(val)
    for j in range(1, i):
        nums[j] = row[i - 1][j - 1] + row[i - 1][j]
    row.append(nums)    
for r in row:
    print(r)
