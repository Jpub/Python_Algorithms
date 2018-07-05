ROWS = 30
COLUMNS = 20

a = [[None] * COLUMNS for i in range(ROWS)]

for i in range(ROWS):
    for j in range(COLUMNS):
        a[i][j] = float(input())

minimum = [None] * ROWS
maximum = [None] * ROWS
for i in range(ROWS):
    minimum[i] = a[i][0]
    maximum[i] = a[i][0]
    for j in range(1, COLUMNS):
        if a[i][j] < minimum[i]:
            minimum[i] = a[i][j]
        if a[i][j] > maximum[i]:
            maximum[i] = a[i][j]

for i in range(ROWS):
    print(minimum[i], maximum[i])