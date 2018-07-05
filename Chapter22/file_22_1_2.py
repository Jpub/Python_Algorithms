import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("정수를 입력하여라: ")

if re.match(IS_NUMERIC, inp):
    x = int(inp)
    if x % 5 == 0 and x % 8 == 0:
        print(x, "은/는 5와 8로 나누어 떨어집니다.")
    else:
        print(x, "은/는 당신이 찾던 수가 아닙니다.")
else:
    print("올바르지 않은 수입니다.")
