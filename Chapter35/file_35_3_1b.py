LAKES = 20

depths = [None] * LAKES
for i in range(LAKES):
    depths[i] = float(input())

maximum = max(depths)
print(maximum)