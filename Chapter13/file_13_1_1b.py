number1 = int(input("첫 번째 숫자를 입력하여라: "))
number2 = int(input("두 번째 숫자를 입력하여라: "))

q, r = divmod(number1, number2)

print("몫값:", q, "\n나머지 값:", r)
