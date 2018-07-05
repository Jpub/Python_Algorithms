import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

total = 0
for i in range(10):
    inp = input("숫자를 입력하여라: ")
    while not re.match(IS_NUMERIC, inp):
        print("숫자를 입력하시오!")
        inp = input("숫자를 입력하여라: ")

    a = float(inp)

    total = total + a

print(total)
