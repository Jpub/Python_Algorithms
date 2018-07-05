N = 5
a = [[None] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            a[i][j] = -1
        elif i > j:
            a[i][j] = 10
        else:
            a[i][j] = 20

for i in range(N):
    for j in range(N):
        print(a[i][j], end = "\t")
    print()