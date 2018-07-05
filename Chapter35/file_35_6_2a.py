DAYS = 31

t = [None] * DAYS

for i in range(DAYS):
    t[i] = int(input())

count = 0
for i in range(DAYS):
    if t[i] < 2:
        count += 1

if count != 0:
    print("강설 가능성이 있습니다.")