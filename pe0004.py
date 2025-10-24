def isPalindrome(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digitsreversed = digits[::-1]
    print(digits)
    print(digitsreversed)
    if digits == digitsreversed:
        return True
    else:
        return False

mx = 0
for i in range(100, 1000):
    for j in range(i + 1, 1000):
        if isPalindrome(i * j):
            mx = max(mx, i * j)
print(mx)

