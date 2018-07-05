CITIES = 10
CITIZENS = 30

phone_num = [[None] * CITIZENS for i in range(CITIES)]
ans = [[None] * CITIZENS for i in range(CITIES)]

for i in range(CITIES):
    print((i + 1), "번째 도시")
    for j in range(CITIZENS):
        phone_num[i][j] = input(str(j + 1) + \
        "번째 시민의 전화번호를 입력하여라: ")
        ans[i][j] = input(str(j + 1) + \
        "번째 시민의 설문 답변을 입력하여라: ").upper()
while ans[i][j] != "Y" and ans[i][j] != "N" and ans[i][j] != "S":
    ans[i][j] = input("잘못된 답변입니다. 답변을 다시 입력하여라: ").upper()

needle = input("찾고자 하는 전화번호를 입력하여라: ")

found = False
position_i = -1
position_j = -1
i = 0
while i <= CITIES - 1 and found == False:
    j = 0
    while j <= CITIZENS - 1 and found == False:
        if phone_num[i][j] == needle:
            found = True
            position_i = i
            position_j = j
            j += 1
            i += 1
            
if found == False:
    print("전화번호를 찾지 못했습니다.")
else:
    print("전화번호", phone_num[position_i][position_j])
    print("를 찾았습니다. '", end = "")

if ans[position_i][position_j] == "Y":
    print("예", end = "")
elif ans[position_i][position_j] == "N":
    print("아니요", end = "")
else:
    print("불확실", end = "")

print("' 설문결과입니다.")