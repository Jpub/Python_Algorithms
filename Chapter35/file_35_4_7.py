TEAMS = 32
PLAYERS = 24

# 팀 이름, 선수 이름, 선수별 득점수를 함께 읽어 들인다.
t = [None] * TEAMS
p = [ [None] * PLAYERS for i in range(TEAMS) ]
g = [ [None] * PLAYERS for i in range(TEAMS) ]
for i in range(TEAMS):
    t[i] = input(str(i + 1) + "번째 팀의 이름을 입력하여라: ")
    for j in range(PLAYERS):
        p[i][j] = input(str(j + 1) + "번째 선수의 이름을 입력하여라: ")
        g[i][j] = int(input(str(j + 1) + "번째 선수의 득점수를 입력하여라: "))
        
# 리스트 g를 정렬한다.
for i in range(TEAMS):
    m = 0
    swaps = True
    while m < PLAYERS - 1 and swaps == True:
        swaps = False
        for n in range(PLAYERS - 1, m, -1):
            if g[i][n] > g[i][n - 1]:
                g[i][n], g[i][n - 1] = g[i][n - 1], g[i][n]
                p[i][n], p[i][n - 1] = p[i][n - 1], p[i][n]
                swaps = True
        m += 1

# 각 팀별 최고 득점자 5명을 출력한다.
for i in range(TEAMS):
    print(t[i] + "팀의 최고 득점자")
    print("----------------------------------")
    for j in range(5):
        print(p[i][j], "선수가", g[i][j], "득점을 하였습니다.")
