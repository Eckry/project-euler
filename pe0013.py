numbers = []
for i in range(100):
    numbers.append(int(input()))

sm = 0
for num in numbers:
    sm += num
print(sm)
