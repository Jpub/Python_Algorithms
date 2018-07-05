ROWS = 30
COLUMNS = 20

a = [[None] * COLUMNS for i in range(ROWS)]

for i in range(ROWS):
    for j in range(COLUMNS):
        a[i][j] = float(input())

for j in range(COLUMNS):
    minimum = a[0][j]
    maximum = a[0][j]
    for i in range(1, ROWS):
        if a[i][j] < minimum:
            minimum = a[i][j]
        if a[i][j] > maximum:
            maximum = a[i][j]
    print(minimum, maximum)