def minimum(val1, val2, val3):

    minim = val1
    if val2 < minim:
        minim = val2
    if val3 < minim:
        minim = val3
    print(minim)

# 메인 코드가 여기서 시작된다.
a = float(input())
b = float(input())
c = float(input())

minimum(a, b, c)
print("종료")
