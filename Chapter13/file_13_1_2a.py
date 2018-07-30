number = int(input("네 자리 정수를 입력하여라: "))

digit1 = number // 1000
r = number % 1000

digit2 = r // 100
r = r % 100

digit3 = r // 10
digit4 = r % 10

total = digit1 + digit2 + digit3 + digit4
print(total)