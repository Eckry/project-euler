# sieve = [1 for _ in range(50000000)]
#
# for i in range(2, 50000000):
#     for j in range(i, 50000000, i):
#         sieve[j] += 1
def cntDivisors(n):
    divisors = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors += 2
        i += 1
    return divisors

triangle = 1
sm = 2
divisors = 0
while divisors < 500:
    triangle += sm
    sm += 1
    divisors = cntDivisors(triangle)
    print(f"Testing {triangle}, result: {divisors}")
