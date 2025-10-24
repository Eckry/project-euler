def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i ==0:
            return False
        i +=1
    return True
cnt = 0
for i in range(2, 1000000):
    if isPrime(i):
        cnt+=1
    if cnt == 10001:
        print(i)
        break
print(cnt)
    
