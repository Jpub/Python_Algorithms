EVENTS = 20
COUNTRIES = 10

country_names = [None] * COUNTRIES
event_descriptions = [ [None] * COUNTRIES for i in range(EVENTS) ]
event_years = [ [None] * COUNTRIES for i in range(EVENTS) ]

for j in range(COUNTRIES):
    country_names[j] = input(str(j + 1) + "번째 국가 이름을 입력하여라: ")
    for i in range(EVENTS):
        event_descriptions[i][j] = input(str(i + 1) + \
        "번째 사건에 대한 설명을 입력하여라: ")
        event_years[i][j] = int(input(str(i + 1) + \
        "번째 사건에 대한 연도를 입력하여라: "))

needle = int(input("찾고자 하는 연도를 입력하여라: "))
row_index = -1

for j in range(COUNTRIES):
    top = 0
    bottom = EVENTS - 1
    found = False
    while top <= bottom and found == False:
        middle = (top + bottom) // 2

if event_years[middle][j] > needle:
    bottom = middle - 1
elif event_years[middle][j] < needle:
    top = middle + 1
else:
    found = True
    row_index = middle

if found == False:
    print(country_names[j], "에 대한 어떤 사건도 발견하지 못했습니다.")
else:
    print("국가:", country_names[j])
    print("연도:", event_years[row_index][j])
    print("사건:", event_descriptions[row_index][j])