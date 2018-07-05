COLUMNS = 20
ROWS_OF_A = 10
ROWS_OF_B = 30

# 입력받은 값을 리스트 a에 저장한다.
a = [ [None] * COLUMNS for i in range(ROWS_OF_A) ]
for i in range(ROWS_OF_A):
    for j in range(COLUMNS):
        a[i][j] = float(input())

# 입력받은 값을 리스트 b에 저장한다.
b = [ [None] * COLUMNS for i in range(ROWS_OF_B) ]
for i in range(ROWS_OF_B):
    for j in range(COLUMNS):
        b[i][j] = float(input())

# 리스트 new_arr를 생성한다.
new_arr = a + b

# 리스트 new_arr를 출력한다.
for row in new_arr:
    for element in row:
        print(element, end = "\t")
    print()