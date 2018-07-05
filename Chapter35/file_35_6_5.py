import math

ATHLETES = 20
SHOTS = 6

# 리스트 names와 points에 값을 입력받는다.
names = [None] * ATHLETES
points = [[None] * SHOTS for i in range(ATHLETES)]

for i in range(ATHLETES):
    names[i] = input(str(i + 1) + "번째 선수의 이름을 입력하여라: ")
    for j in range(SHOTS):
        points[i][j] = int(input(str(j + 1) + \
        "번째 화살의 득점을 입력하여라: "))

# 리스트 total을 생성한다.
total = []
for row in points:
    total.append(math.fsum(row))

# 리스트 names와 total을 정렬한다.
for m in range(1, ATHLETES):
    for n in range(ATHLETES - 1, m - 1, -1):
        if total[n] > total[n - 1]:
            total[n], total[n - 1] = total[n - 1], total[n]
            names[n], names[n - 1] = names[n - 1], names[n]

# 금메달, 은메달, 동메달 수여자를 출력한다.
for i in range(3):
    print(names[i], "\t", total[i])