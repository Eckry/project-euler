x = 2 ** 1000
sm = 0
while x:
    sm += x % 10
    x //= 10
print(sm)
