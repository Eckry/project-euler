sm = 2
first = 1
second = 2
while second <= 4000000:
    first, second = second, first + second
    if second % 2 == 0:
        sm += second
print(sm)
