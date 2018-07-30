ROWS = 5
COLUMNS = 7

a = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        print(i, ",", j, "의 요솟값을 입력하여라: ")
        a[i][j] = float(input())

for i in range(ROWS):
    for j in range(COLUMNS):
        if a[i][j] != int(a[i][j]):
            print(i, ",", j, "위치에서 실수가 발견되었습니다.")
