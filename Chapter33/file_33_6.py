ROWS = 3
COLUMNS = 4
ELEMENTS = ROWS * COLUMNS

a = [None] * ELEMENTS

for k in range(ELEMENTS):
    a[k] = int(input(str(k) + " 요소의 값을 입력하여라: "))

b = [ [None] * COLUMNS for i in range(ROWS) ]
k = 0 # 리스트 a의 인덱스

for j in range(COLUMNS): # 열 단위로 반복
    for i in range(ROWS):
        b[i][j] = a[k]
        k += 1

for i in range(ROWS): # 행 단위로 반복
    for j in range(COLUMNS):
        print(b[i][j], end = "\t")
    print()
