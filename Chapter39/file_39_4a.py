ELEMENTS = 10

def get_list(a):
    for m in range(1, ELEMENTS):
        element = a[m]
        n = m
        while n > 0 and a[n - 1] > element:
            a[n] = a[n - 1]
            n -= 1
        a[n] = element

# 메인 코드
t = [75, 73, 78, 70, 71, 74, 72, 69, 79, 77]

get_list(t)

print("가장 작은 수: ", t[0], t[1], t[2])

# 이 단계에서 리스트 t는 정렬되어 있음.
for i in range(ELEMENTS):
    print(t[i], end = "\t")
