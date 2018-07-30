CITIES = 10
DAYS = 31

names = [None] * CITIES
t = [ [None] * DAYS for i in range(CITIES) ]

for i in range(CITIES):
    names[i] = input(str(i + 1) + "번째 도시의 이름을 입력하여라: ")
    for j in range(DAYS):
        t[i][j] = int(input(str(j + 1) + "번째 날짜의 온도를 입력하여라: "))

count = [None] * CITIES

for i in range(CITIES):
    count[i] = 0
    for j in range(DAYS):
        if t[i][j] < 2:
            count[i] += 1

print("1월 중 강설 가능성이 있는 도시:")
for i in range(CITIES):
    if count[i] != 0:
        print(names[i])
