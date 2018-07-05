def formula1(x):
    if x == 5:
        print("오류! 0-나눗셈")
    else:
        y = 3 * x / (x - 5) + (7 - x) / (2 * x)
        print(y)

def formula2(x):
    if x == -2:
        print("오류! 0-나눗셈")
    else:
        y = (45 - x) / (x + 2) + 3 * x
        print(y)

# 메인 코드
x = float(input("x 값을 입력하여라: "))
if x >= 1:
    formula1(x)
else:
    formula2(x)
