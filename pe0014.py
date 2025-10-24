def next(n):
    if n & 1:
        return 3 * n + 1
    return n // 2

ans = 0
mxcnt = 0
for i in range(1, 1000001):
    num = i
    cnt = 0
    print(f"Testing {num}")
    while num != 1:
        cnt += 1
        num = next(num)
    if mxcnt < cnt:
        mxcnt = cnt
        ans = i
print(ans)

