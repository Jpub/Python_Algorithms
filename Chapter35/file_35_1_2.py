ELEMENTS = 20

# 입력받은 값을 리스트 a와 b에 각각 저장한다.
a = [None] * ELEMENTS
b = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = float(input())
for i in range(ELEMENTS):
    b[i] = float(input())

# 리스트 new_arr를 생성한다.
new_arr = [None] * ELEMENTS

for i in range(ELEMENTS):
    if a[i] > b[i]:
        new_arr[i] = a[i]
    else:
        new_arr[i] = b[i]

# 리스트 new_arr를 출력한다.
for i in range(ELEMENTS):
    print(new_arr[i])