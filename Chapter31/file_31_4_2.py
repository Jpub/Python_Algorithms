ELEMENTS = 5

values = [None] * ELEMENTS

for i in range(ELEMENTS):
    values[i] = float(input())
for value in values[::-1]:
    if value > 0:
        print(value)
