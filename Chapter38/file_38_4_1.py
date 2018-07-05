def display_abs(n):
    if n < 0:
        n = (-1) * n
    print(n)

# 메인 코드가 여기서 시작된다.
a = float(input())
display_abs(a)      #입력값에 대한 절댓값을 출력한다.
print(a)            #입력값을 출력한다.
