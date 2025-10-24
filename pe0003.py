def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

i = 2
res = -1
while i * i <= 600851475143:
    if 600851475143 % i == 0 and isPrime(i):
        res = i
    i += 1
if res == -1:
    print(600851475143)
else:
    print(res)
