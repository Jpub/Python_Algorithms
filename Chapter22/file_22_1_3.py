import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("숫자를 입력하여라: ")

if re.match(IS_NUMERIC, inp):
    x = float(inp)
    if x == int(x):
        print(x, "은/는 정수입니다.")
    else:
        print(x, "은/는 실수입니다.")
else:
    print("숫자가 아닙니다.")
