PEOPLE = 100
# 두 리스트 first_names와 last_names에 저장할 값을 읽어 들인다.
first_names = [None] * PEOPLE
last_names = [None] * PEOPLE
for i in range(PEOPLE):
    first_names[i] = input(str(i + 1) + "번째 사람의 영문 이름: ")
    last_names[i] = input(str(i + 1) + "번째 사람의 영문 성: ")

# 리스트 last_names와 first_names를 정렬시킨다.
for m in range(PEOPLE - 1):
    for n in range(PEOPLE - 1, m, -1):
        if last_names[n] < last_names[n - 1]:
            last_names[n], last_names[n - 1] = \
            last_names[n - 1], last_names[n]
            first_names[n], first_names[n - 1] = \
            first_names[n - 1], first_names[n]
        elif last_names[n] == last_names[n - 1]:
            if first_names[n] < first_names[n - 1]:
                first_names[n], first_names[n - 1] = \
                first_names[n - 1], first_names[n]

# 리스트 last_names와 first_names를 출력한다.
for i in range(PEOPLE):
    print(last_names[i], "\t", first_names[i])