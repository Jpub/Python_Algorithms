CITIES = 10
DAYS = 31

names = [None] * CITIES
t = [ [None] * DAYS for i in range(CITIES) ]

for i in range(CITIES):
    names[i] = input(str(i + 1) + "번째 도시의 이름을 입력하여라: ")
    for j in range(DAYS):   
        t[i][j] = int(input(str(j + 1) + "번째 날짜의 온도를 입력하여라: "))
        
print("1월 중 강설 가능성이 있는 도시:")
for i in range(CITIES):
    found = False
    for j in range(DAYS):
        if t[i][j] < 2:
            found = True
            
    if found == True:
        print(names[i])
