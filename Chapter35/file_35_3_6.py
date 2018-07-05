CITIES = 10
DAYS = 31

names = [None] * CITIES
t = [ [None] * DAYS for i in range(CITIES) ]
for i in range(CITIES):
    names[i] = input()
for j in range(DAYS):
    t[i][j] = int(input())

minimum = t[0][0]
m_i = 0
m_j = 0
for i in range(CITIES):
    for j in range(DAYS):
        if t[i][j] < minimum:
            minimum = t[i][j]
            m_i = i
            m_j = j
            
print("최저 온도:", minimum)
print("도시:", names[m_i])
print("날짜:", m_j + 1)
