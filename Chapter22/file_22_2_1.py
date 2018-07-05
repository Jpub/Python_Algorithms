x = float(input())

if x == 0 or x == 4:
    print("오류: 0-나눗셈")
else:
    y = (5 + x) / x + (x + 9) / (x - 4)
    print(y)
