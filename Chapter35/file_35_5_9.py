EVENTS = 20
COUNTRIES = 10

country_names = [None] * COUNTRIES
event_descriptions = [ [None] * COUNTRIES for i in range(EVENTS) ]

for j in range(COUNTRIES):
    country_names[j] = input(str(j + 1) + "번째 국가를 입력하여라: ")
    for i in range(EVENTS):
        event_descriptions[i][j] = input(str(i + 1) + \
            "번째 사건의 설명을 입력하여라: ")

needle = input("겸색할 국가를 입력하여라: ").upper()

index_position = -1
left = 0
right = EVENTS - 1
found = False
while left <= right and found == False:
    middle = (left + right) // 2

    if country_names[middle].upper() > needle:
        right = middle - 1
    elif country_names[middle].upper() < needle:
        left = middle + 1
    else:
        found = True
        index_position = middle

if found == False:
    print("어떤 국가도 찾지 못하였습니다.")
else:
    for i in range(EVENTS):
        print(event_descriptions[i][index_position])