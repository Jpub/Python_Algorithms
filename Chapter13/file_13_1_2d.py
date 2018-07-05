number = int(input("네 자리 정수를 입력하여라: "))

digit4 = number % 10
r = number // 10

digit3 = r % 10
r = r // 10

digit2 = r % 10
digit1 = r // 10

total = digit1 + digit2 + digit3 + digit4
print(total)
