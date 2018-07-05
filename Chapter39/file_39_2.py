def add(number1, number2):
    result = number1 + number2
    return result

def display_sum(num1, num2):
    print(add(num1, num2))

# 메인 코드
a = int(input())
b = int(input())

display_sum(a, b)
