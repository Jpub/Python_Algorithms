import math
import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

while True:
    inp = input("음수가 아닌 숫자를 입력하여라: ")
    if re.match(IS_NUMERIC, inp) and float(inp) >= 0: break

x = float(inp)

y = math.sqrt(x)
print(y)
