x = float(input("x 값을 입력하여라: "))

if -5 < x <= 0:
    if x != -1:
        y = x / (x - 3) + (8 + x) / (x + 1)
        print(y)
    else:
        print("올바르지 않은 값입니다.")
elif 0 < x <= 6:
    y = 40 * x / (x - 8)
    print(y)
elif 6 < x <= 20:
    if x != 9:
        y = 3 * x / (x - 9)
        print(y)
    else:
        print("올바르지 않은 값입니다.")
else:
    y = abs(x)
    print(y)
