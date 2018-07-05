ELEMENTS = 50

values = [None] * ELEMENTS

total = 0
for i in range(ELEMENTS):
    values[i] = float(input())
    total = total + values[i]

print(total)