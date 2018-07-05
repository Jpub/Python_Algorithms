n1 = int(input("첫 번째 정수를 입력하여라: "))
n2 = int(input("두 번째 정수를 입력하여라: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("두 수 모두 짝수입니다.")
elif n1 % 2 != 0 and n2 % 2 != 0:
    print("두 수 모두 홀수입니다.")
else:
    print("특별하지 않네요!")
