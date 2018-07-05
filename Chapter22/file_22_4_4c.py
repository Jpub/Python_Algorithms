x = float(input("x 값을 입력하여라: "))

if x == -1 or x == 9:
    print("올바르지 않은 값입니다.")
else:
    if x <= -5 or x > 20:
        y = abs(x)
    elif x <= 0:
        y = x / (x - 3) + (8 + x) / (x + 1)
    elif x <= 6:
        y = 40 * x / (x - 8)
    else:
        y = 3 * x / (x - 9)
    print(y)
