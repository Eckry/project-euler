sqsm = 0
sm = 0
for i in range(1, 101):
    sm += i
for i in range(1, 101):
    sqsm += i * i

print(sm ** 2 - sqsm)
