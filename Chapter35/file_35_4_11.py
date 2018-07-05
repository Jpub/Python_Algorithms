CARS = 10
LAPS = 20

# 이름과 경과 시간을 함께 입력받는다.
names = [None] * CARS
elapsed_times = [ [None] * LAPS for i in range(CARS) ]
for i in range(CARS):
    names[i] = input(str(i + 1) + "번째 운전자의 이름을 입력하여라: ")
    for j in range(LAPS):
        elapsed_times[i][j] = float(input(str(j + 1) + \
        "번째 바퀴의 경과 시간을 입력하여라: "))

# 리스트 elapsed_times를 정렬한다.
for i in range(CARS):
    for m in range(1, LAPS):
        element = elapsed_times[i][m]
        n = m
        while n > 0 and elapsed_times[i][n - 1] > element:
            elapsed_times[i][n] = elapsed_times[i][n - 1]
            n -= 1
        elapsed_times[i][n] = element

# 가장 오래 걸린 경과 시간 세 개를 출력한다.
for i in range(CARS):
    print(names[i], "의 가장 오래 걸린 경과 시간")
    print("-------------------------------------")
    for j in range(3):
        print(elapsed_times[i][j])