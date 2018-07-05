def Fib(n):
    if n == 0 or n == 1:
        return_value = n
    else:
        return_value = Fib(n - 1) + Fib(n - 2)

    return return_value

# 메인 코드
num = int(input())
print(Fib(num))
