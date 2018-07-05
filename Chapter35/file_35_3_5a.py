CITIES = 10
DAYS = 31

# 입력받은 값을 리스트 t에 저장한다.
t = [ [None] * DAYS for i in range(CITIES) ]
for i in range(CITIES):
    for j in range(DAYS):
        t[i][j] = int(input())

# 최솟값을 찾는다.
minimum = t[0][0]
for i in range(CITIES):
    for j in range(DAYS):
        if t[i][j] < minimum:
            minimum = t[i][j]

print(minimum)