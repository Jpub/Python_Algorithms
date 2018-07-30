import math

print("a, b, c의 값을 입력하여라: ")
a = float(input())
b = float(input())
c = float(input())

if a != 0:
    D = b ** 2 - 4 * a * c
    if D >= 0:
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print("근:", x1, ",", x2)
        else:
            x = -b / (2 * a)
            print("하나의 중근:", x)
    else:
        print("허근")
else:
    if b != 0:
        x = -c / b
        print("근:", x)
    elif c != 0:
        print("불능")
    else:
        print("부정")
