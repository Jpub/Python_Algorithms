LAKES = 20

names = [None] * LAKES
areas = [None] * LAKES

for i in range(LAKES):
    names[i] = input()
    areas[i] = float(input())

for m in range(LAKES - 1):
    for n in range(LAKES - 1, m, -1):
        if areas[n] < areas[n - 1]:
            areas[n], areas[n - 1] = areas[n - 1], areas[n]
            names[n], names[n - 1] = names[n - 1], names[n]

for i in range(LAKES):
    print(names[i], "\t", areas[i])