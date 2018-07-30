import re

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"
ELEMENTS = 20
odds = [None] * ELEMENTS
for i in range(ELEMENTS):
    while True:
        inp = input("홀수 정수를 입력하여라: ")
        failure = False
        if not re.match(IS_NUMERIC, inp):
            print("숫자값을 입력하여라!")
            failure = True
        elif float(inp) != int(float(inp)):
            print("정수를 입력하여라!")
            failure = True
        elif int(inp) % 2 == 0:
            print("홀수를 입력하세요!")
            failure = True
        if failure == False: break
    odds[i] = int(inp)

# 요소를 역순으로 출력
for element in odds[::-1]:
    print(element, end = "\t")
