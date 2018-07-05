ROWS = 30
COLUMNS = 20

a = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        a[i][j] = float(input())

for i in range(ROWS):
    minimum = a[i][0]
    maximum = a[i][0]
    for j in range(1, COLUMNS):
        if a[i][j] < minimum:
            maximum = a[i][j]
        if a[i][j] > maximum:
            maximum = a[i][j]
            
    print(minimum, maximum)