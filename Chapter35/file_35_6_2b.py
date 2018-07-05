DAYS = 31

t = [None] * DAYS

for i in range(DAYS):
    t[i] = int(input())

found = False
for i in range(DAYS):
    if t[i] < 2:
        found = True

if found == True:
    print("강설 가능성이 있습니다.")