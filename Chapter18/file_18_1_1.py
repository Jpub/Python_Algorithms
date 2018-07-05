a = int(input())
b = int(input())

if a > 3:
    print("변수 A는 3보다 큽니다")
elif a > 4 and b <= 10:
    print("변수 A는 4보다 크고 ")
    print("변수 B는 10보다 작거나 같습니다.")
elif a * 2 == -26:
    print("변수 A 곱하기 2는 -26과 같습니다.")
    b += 1
elif b == 1:
    print("변수 B는 1과 같습니다.")
else:
    print("위의 모든 불리언 식이 False일 경우 ")
    print("이 메시지가 표시됩니다.")

print("종료!")
