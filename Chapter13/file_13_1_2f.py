number = int(input("다섯 자리 정수를 입력하여라: "))

r, digit5 = divmod(number, 10)
r, digit4 = divmod(r, 10)
r, digit3 = divmod(r, 10)
digit1, digit2 = divmod(r, 10)

print(digit1, digit2, digit3, digit4, digit5) 
