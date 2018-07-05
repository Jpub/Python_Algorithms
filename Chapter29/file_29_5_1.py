import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

maximum = -1

for i in range(10):
    inp = input("몸무게 값을 입력하여라: ")
    while not re.match(IS_NUMERIC, inp) or float(inp) < 0    \
          or float(inp) > 680:
        
        inp = input("부적절한 값! 1과 680 사이의 몸무게 값을 입력하여라: ")

    w = int(inp)

    if w > maximum:
        maximum = w

print(maximum)
