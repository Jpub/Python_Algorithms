ELEMENTS_OF_A = 20
ELEMENTS_OF_B = 30
ELEMENTS_OF_NEW = ELEMENTS_OF_A + ELEMENTS_OF_B

# 입력받은 값을 리스트 a와 b에 각각 저장한다.
a = [None] * ELEMENTS_OF_A
b = [None] * ELEMENTS_OF_B
for i in range(ELEMENTS_OF_A):
    a[i] = float(input())
for i in range(ELEMENTS_OF_B):
    b[i] = float(input())
# 리스트 new_arr를 생성한다.
new_arr = [None] * ELEMENTS_OF_NEW
for i in range(ELEMENTS_OF_A):
    new_arr[i] = a[i]
for i in range(ELEMENTS_OF_B):
    new_arr[ELEMENTS_OF_A + i] = b[i]

# 리스트 new_arr를 출력한다.
for i in range(ELEMENTS_OF_NEW):
    print(new_arr[i], end = "\t")