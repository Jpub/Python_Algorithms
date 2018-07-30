ROWS = 30
COLUMNS = 20

a = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        a[i][j] = float(input())

minimum = [None] * COLUMNS
maximum = [None] * COLUMNS

for j in range(COLUMNS):
    minimum[j] = a[0][j]
    maximum[j] = a[0][j]
    for i in range(1, ROWS):
        if a[i][j] < minimum[j]:
            minimum[j] = a[i][j]
        if a[i][j] > maximum[j]:
            maximum[j] = a[i][j]

for j in range(COLUMNS):
    print(minimum[j], maximum[j])