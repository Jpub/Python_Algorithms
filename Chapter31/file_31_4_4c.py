import math
ELEMENTS = 50

values = [None] * ELEMENTS
for i in range(ELEMENTS):
    values[i] = float(input())

total = math.fsum(values)

print(total)