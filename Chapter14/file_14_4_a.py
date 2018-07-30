number = int(input("정수를 입력하여라: "))

# 숫자를 문자열로 바꾼다.
number_string = str(number)

# 문자열을 역순으로 바꾼다.
reversed_string = number_string[::-1]

# 역순으로 바꿔진 문자열을 정수로 바꾼다.
reversed_number = int(reversed_string)

print(reversed_number)
