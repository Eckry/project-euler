pyramid = []
ans = []
for i in range(15):
    row = list(map(int, input().split()))
    ans.append([0] * len(row))
    pyramid.append(row)

ans[0][0] = pyramid[0][0] 
for idx, row in enumerate(pyramid):
    if idx == len(pyramid) - 1:
        continue
    for i, num in enumerate(row):
        left = i
        right = i + 1
        ans[idx + 1][left] = max(ans[idx + 1][left], ans[idx][i] + pyramid[idx + 1][left])
        ans[idx + 1][right] = max(ans[idx + 1][right], ans[idx][i] + pyramid[idx + 1][right])
print(max(ans[len(ans) - 1]))





