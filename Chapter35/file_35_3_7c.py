ROWS = 30
COLUMNS = 20

a = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        a[i][j] = float(input())

for row in a:
    print(min(row), max(row))