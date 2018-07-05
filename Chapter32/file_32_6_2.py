N = 5
a = [[None] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        a[i][j] = float(input())

# total 계산
total = 0
for i in range(N):
    j = N - i - 1
    total = total + a[i][j]

print("총합:", total)
