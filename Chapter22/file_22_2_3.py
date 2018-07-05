import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input()

if re.match(IS_NUMERIC, inp):
    x = float(inp)
    if x >= 0 :
        if x == 0 or x == 3:
            print("오류: 0-나눗셈")
        else:
            y = (7 + x) / (x - 3) + (3 - x) / x
            print(y)
    else:
        y = 40 * x / (x - 5) + 3
        print(y)
else:
    print("숫자가 아닙니다.")
