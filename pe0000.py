sm = 0
for i in range(1, 198001):
    if((i * i) & 1):
        sm += i * i

print(sm)
