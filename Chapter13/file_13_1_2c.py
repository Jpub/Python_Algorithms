number = int(input("여섯 자리 정수를 입력하여라: "))

digit1, r = divmod(number, 100000)
digit2, r = divmod(r, 10000)
digit3, r = divmod(r, 1000)
digit4, r = divmod(r, 100)
digit5, digit6 = divmod(r, 10)

print(digit1, digit2, digit3, digit4, digit5, digit6)
