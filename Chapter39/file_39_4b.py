ELEMENTS = 10

def get_list(a):
    aux_list = [None] * ELEMENTS

    # 리스트를 보조 리스트에 복사한다.
    for m in range(ELEMENTS):
        aux_list[m] = a[m]

    # 보조 리스트를 정렬한다.
    for m in range(1, ELEMENTS):
        element = aux_list[m]
        n = m
        while n > 0 and aux_list[n - 1] > element:
            aux_list[n] = aux_list[n - 1]
            n -= 1
        aux_list[n] = element

    ret_list = [aux_list[0], aux_list[1], aux_list[2]]
    return ret_list

# 메인 코드
names = ["도시1", "도시2", "도시3", "도시4", "도시5",   \
         "도시6", "도시7", "도시8", "도시9", "도시10"]

t = [75, 73, 78, 70, 71, 74, 72, 69, 79, 77]

low = get_list(t)
print("가장 낮은 온도: ", low[0], low[1], low[2])

# 이 단계에서 리스트 t는 정렬되어 있지 않음
for i in range(ELEMENTS):
    print(t[i], "\t", names[i])
