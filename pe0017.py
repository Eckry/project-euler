numbers = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
ans = 0

for i in range(1, 1000):
    name = ""
    if 11 <= i and i <= 19:
        name += numbers[i]
    else:
        if i % 100 == 0:
            cnt = i // 100
            name = f"{numbers[cnt]}hundred"
        elif i >= 100:
            cnt = i // 100
            name = f"{numbers[cnt]}hundredand"
            
        if 11 <= i% 100 and i % 100 <= 19:
            name += numbers[i % 100]
        else:
            cnt = (i % 100) - i % 10
            name += f"{numbers[cnt]}"
            name += f"{numbers[i % 10]}"

    ans += len(name)
    print(name)

ans += len("onethousand")
print(ans)
