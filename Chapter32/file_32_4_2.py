ROWS = 5
COLUMNS = 7

a = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        print(i, ",", j, "요솟값을 입력하여라: ")
        a[i][j] = float(input())

# 열을 따라 반복 처리
for j in range(1, COLUMNS, 2): # 1부터 시작하여 2만큼씩 증가
    for i in range(ROWS):
        print(a[i][j])
