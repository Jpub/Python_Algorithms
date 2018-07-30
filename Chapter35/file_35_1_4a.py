COLUMNS = 20
ROWS_OF_A = 10
ROWS_OF_B = 30
ROWS_OF_NEW = ROWS_OF_A + ROWS_OF_B

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
        
# 리스트 new_arr를 저장한다.
new_arr = [ [None] * COLUMNS for i in range(ROWS_OF_NEW) ]
for i in range(ROWS_OF_A):
    for j in range(COLUMNS):
        new_arr[i][j] = a[i][j]
for i in range(ROWS_OF_B):
    for j in range(COLUMNS):
        new_arr[ROWS_OF_A + i][j] = b[i][j]
        
# 리스트 new_arr를 출력한다.
for i in range(ROWS_OF_NEW):
    for j in range(COLUMNS):
        print(new_arr[i][j], end = "\t")
    print()