ELEMENTS = 100
values = [None] * ELEMENTS

for i in range(ELEMENTS):
    values[i] = int(input())

for i in range(ELEMENTS):
    if i % 2 != 0 and values[i] % 2 == 0:
        print(values[i])