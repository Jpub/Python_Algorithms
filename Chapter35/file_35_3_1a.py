LAKES = 20

depths = [None] * LAKES
for i in range(LAKES):
    depths[i] = float(input())

# 초깃값
maximum = depths[0]
# 위치 1부터 검색한다.
for i in range(1, LAKES):
    if depths[i] > maximum:
        maximum = depths[i]
    
print(maximum)