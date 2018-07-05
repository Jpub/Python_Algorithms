number = int(input("다섯 자리 정수를 입력하여라: "))

digit5 = number % 10
r = number // 10

digit4 = r % 10
r = r // 10

digit3 = r % 10
r = r // 10

digit2 = r % 10
digit1 = r // 10

print(digit1, digit2, digit3, digit4, digit5)
