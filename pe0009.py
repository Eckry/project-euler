flg = 1
for i in range(1, 1000):
    for j in range(i + 1, 1000):
        for k in range(j + 1, 1000):
            if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                flg = 0
                print(i * j * k)
                break
        if not flg:
            break
    if not flg:
        break

