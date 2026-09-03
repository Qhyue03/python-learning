big = []
for i in range(3):
    row = []
    for j in range(3):
        val = (i + 1) * 3 - j
        row.append(val)
    big.append(row)

print(big)
