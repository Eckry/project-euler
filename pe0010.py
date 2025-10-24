sieve = [1 for _ in range(2000001)]

sm = 0
for i in range(2, 2000001):
    if not sieve[i]:
        continue
    sm += i
    for j in range(i * 2, 2000001, i):
        sieve[j] = 0
print(sm)

