ELEMENTS = 100

values = [None] * ELEMENTS

for i in range(ELEMENTS):
    values[i] = int(input())

for i in range(1, ELEMENTS, 2):
    if values[i] % 2 == 0:
        print(values[i])