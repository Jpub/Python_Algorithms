import math

while True:
    a = float(input("변 A를 입력하여라: "))
    while a <= 0:
        a = float(input("올바르지 않은 값입니다. 변 A를 입력하여라: "))

    b = float(input("변 B를 입력하여라: "))
    while b <= 0:
        b = float(input("올바르지 않은 값입니다. 변 B를 입력하여라: "))

    c = float(input("변 C를 입력하여라: "))
    while c <= 0:
        c = float(input("올바르지 않은 값입니다. 변 C를 입력하여라: "))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("면적:", area)

    answer = input("반복하시겠습니까?: ")
    if answer.upper() != "YES": break
