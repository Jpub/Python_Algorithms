import math
import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("음수가 아닌 숫자를 입력하여라: ")
while not re.match(IS_NUMERIC, inp) or float(inp) < 0:
    print("오류: 올바르지 않은 입력값입니다.")
    inp = input("음수가 아닌 숫자를 입력하여라: ")

x = float(inp)

y = math.sqrt(x)
print(y)
