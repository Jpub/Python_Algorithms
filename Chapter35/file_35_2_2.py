import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

ELEMENTS = 20

odds = [None] * ELEMENTS
for i in range(ELEMENTS):
    inp = input("홀수 정수를 입력하여라: ")
    while not re.match(IS_NUMERIC, inp) or int(inp) % 2 == 0:
        print("부적절한 값!")
        inp = input("홀수 정수를 입력하여라: ")
    odds[i] = int(inp)

# 요소를 역순으로 출력
for element in odds[::-1]:
    print(element, end = "\t")
