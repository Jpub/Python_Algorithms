import math
import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

while True:
    inp = input("음수가 아닌 숫자를 입력하여라: ")

    failure = False
    if not re.match(IS_NUMERIC, inp):
        print("숫자를 입력하시오!")
        failure = True
    elif float(inp) < 0:
        print("음수가 아닌 숫자를 입력하시오!")
        failure = True
        
    if failure == False: break

x = float(inp)

y = math.sqrt(x)
print(y)
