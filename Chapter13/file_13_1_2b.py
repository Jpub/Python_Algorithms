number = int(input("여섯 자리 정수를 입력하여라: "))

digit1 = number // 100000
r = number % 100000

digit2 = r // 10000
r = r % 10000

digit3 = r // 1000
r = r % 1000

digit4 = r // 100
r = r % 100

digit5 = r // 10
digit6 = r % 10

print(digit1, digit2, digit3, digit4, digit5, digit6)
