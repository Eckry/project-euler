digits = []
for i in range(20):
    digits.append(list(map(int, input().split(" "))))

mx = 0
for i in range(20):
    for j in range(20):
        mlt = 1
        if j + 4 < 20:
            for k in range(j, j + 4):
                mlt *= digits[i][k]
        mx = max(mx, mlt)
        mlt = 1
        if i + 4 < 20:
            for k in range(i, i + 4):
                mlt *= digits[k][j]
        mx = max(mx, mlt)
        mlt = 1
        if i + 4 < 20 and j + 4 < 20:
            for k in range(4):
                mlt *= digits[i + k][j + k]
        mx = max(mx, mlt)
        mlt = 1
        if i + 4 < 20 and j - 4 >= 0:
            for k in range(4):
                mlt *= digits[i + k][j - k]
        mx = max(mx, mlt)

print(mx)


            

