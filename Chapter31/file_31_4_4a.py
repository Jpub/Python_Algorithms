ELEMENTS = 50

values = [None] * ELEMENTS
for i in range(ELEMENTS):
    values[i] = float(input())

total = 0
for i in range(ELEMENTS):
    total = total + values[i]

print(total)