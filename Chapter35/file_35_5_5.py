TEAMS = 20
WEEKS = 12

names = [None] * TEAMS
results = [ [None] * WEEKS for i in range(TEAMS) ]

for i in range(TEAMS):
    names[i] = input(str(i + 1) + "번째 팀 이름을 입력하여라: ")
    for j in range(WEEKS):
        results[i][j] = input(str(j + 1) + "번째 주 " + names[i] + \
        "의 결과를 입력하여라: ")
        needle = input("찾고자 하는 결과를 입력하여라: ")

for i in range(TEAMS):
    found = False
    print(names[i], "의 결과를 발견하였습니다.")
    for j in range(WEEKS):
        if results[i][j].upper() == needle.upper():
            print((j + 1), "번째 주")
            found = True

if found == False:
    print("어떤 결과도 발견하지 못했습니다.")