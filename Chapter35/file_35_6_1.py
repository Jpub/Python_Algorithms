DAYS = 31

t = [None] * DAYS

for i in range(DAYS):
    t[i] = int(input())

for i in range(DAYS):
    if t[i] < 2:
        print(i + 1, end = "\t")