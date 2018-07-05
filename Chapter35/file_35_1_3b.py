ELEMENTS_OF_A = 20
ELEMENTS_OF_B = 30

# 입력받은 값을 리스트 a와 b에 각각 저장한다.
a = [None] * ELEMENTS_OF_A
b = [None] * ELEMENTS_OF_B
for i in range(ELEMENTS_OF_A):
    a[i] = float(input())
for i in range(ELEMENTS_OF_B):
    b[i] = float(input())

# 리스트 new_arr를 생성한다.
new_arr = []
for element in a:
    new_arr.append(element)
for element in b:
    new_arr.append(element)

# 리스트 new_arr를 출력한다.
for element in new_arr:
    print(element, end = "\t")