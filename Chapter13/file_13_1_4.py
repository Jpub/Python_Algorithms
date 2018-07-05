number = int(input("세 자리 정수를 입력하여라: "))

digit3 = number % 10    # 가장 오른쪽 자릿수값
r = number // 10

digit2 = r % 10        # 중간 자릿수값
digit1 = r // 10          # 가장 왼쪽 자릿수값

reversed_number = digit3 * 100 + digit2 * 10 + digit1
print(reversed_number)
