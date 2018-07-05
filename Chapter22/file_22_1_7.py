a = float(input("첫 번째 피연산자 값을 입력하여라: "))
op = input("연산자 유형을 입력하여라: ")
b = float(input("두 번째 피연산자 값을 입력하여라: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("오류: 0-나눗셈")
    else:
        print(a / b)
