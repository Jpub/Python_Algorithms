x = float(input("x 값을 입력하여라: "))

if x == -1 or x == 9:
    print("올바르지 않은 값입니다.")
else:
    if -5 < x <= 0:
        y = x / (x - 3) + (8 + x) / (x + 1)
    elif 0 < x <= 6:
        y = 40 * x / (x - 8)
    elif 6 < x <= 20:
        y = 3 * x / (x - 9)
    else:
        y = abs(x)
    print(y)
