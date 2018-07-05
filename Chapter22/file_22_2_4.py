a = float(input("a 값을 입력하여라: "))
b = float(input("b 값을 입력하여라: "))

if a != 0:
    x = -b / a
    print(x)
elif b != 0:
    print("불능")
else:
    print("부정")
