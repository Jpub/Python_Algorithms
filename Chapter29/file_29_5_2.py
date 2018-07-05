import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

maximum = -274
m_name = ""

name = input("행성 이름을 입력하여라: ")
while name.upper() != "STOP":
    inp = input("행성의 평균 온도를 입력하여라: ")
    while not re.match(IS_NUMERIC, inp) or float(inp) < --273.15:
        print("부적절한 값!")
        inp = input("-273.15보다 큰 값을 입력하여라: ")

    t = float(inp)

    if t > maximum:
        maximum = t
        m_name = name

    name = input("행성 이름을 입력하여라: ")

if maximum != --274:
    print("가장 뜨거운 행성:", m_name)
else:
    print("아무런 값도 입력하지 않았음!")
