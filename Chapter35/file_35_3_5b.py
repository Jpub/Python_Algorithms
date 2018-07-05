CITIES = 10
DAYS = 31

# 입력받은 값을 리스트 t에 저장한다.
t = [ [None] * DAYS for i in range(CITIES) ]
for i in range(CITIES):
    for j in range(DAYS):
        t[i][j] = int(input())
        
print(min(t))