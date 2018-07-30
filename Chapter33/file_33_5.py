ROWS = 3
COLUMNS = 4
ELEMENTS = ROWS * COLUMNS

a = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        a[i][j] = int(input(str(i) + ", " + str(j) + " 요소의 값을 입력하여라: "))

b = [None] * ELEMENTS

k = 0 # 새로운 리스트의 인덱스

for j in range(COLUMNS): # 열 단위로 반복
    for i in range(ROWS):
        b[k] = a[i][j]
        k += 1

for k in range(ELEMENTS):
    print(b[k], end = "\t")
