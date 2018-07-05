def factorial(value):
    if value == 1:
        return_value = 1
    else:
        return_value = value * factorial(value - 1)

    return return_value

# 메인 코드
print(factorial(5)) # 120 출력
