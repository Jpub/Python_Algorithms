import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("정수를 입력하여라: ")

if re.match(IS_NUMERIC, inp):
    x = int(inp)
    if x % 5 == 0 and x % 8 == 0:
        print(x, "5와 8로 나누어떨어집니다.")
    else:
        print(x, "은/는 당신이 찾는 숫자가 아닙니다.")
else:
    print("숫자가 아닙니다.")
