def get_list(a):
    return sorted(a)[0:3]

# 메인 코드
names = ["도시1", "도시2", "도시3", "도시4", "도시5",   \
         "도시6", "도시7", "도시8", "도시9", "도시10"]

t = [75, 73, 78, 70, 71, 74, 72, 69, 79, 77]

low = get_list(t)
print("가장 낮은 온도: ", low[0], low[1], low[2])

# 이 단계에서 리스트 t는 정렬되어 있지 않음
for i in range(len(t)):
    print(t[i], "\t", names[i])
