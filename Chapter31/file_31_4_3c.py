ELEMENTS = 100

values = [None] * ELEMENTS

for i in range(ELEMENTS):
    values[i] = int(input())

for value in values[1::2]:
    if value % 2 == 0:
        print(value)