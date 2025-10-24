sz = 21
grid = [[0 for _ in range(sz)] for _ in range(sz)]

grid[0][0] = 1
for i in range(sz):
    for j in range(sz):
        if i >= 0:
            grid[i][j] += grid[i - 1][j]
        if j >= 0:
            grid[i][j] += grid[i][j - 1]
print(grid[sz - 1][sz - 1])


