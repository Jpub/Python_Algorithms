ELEMENTS = 20

a = [None] * ELEMENTS

for i in range(ELEMENTS):
    a[i] = float(input())

for m in range(ELEMENTS - 1):
    for n in range(ELEMENTS - 1, m, -1):
        if a[n] < a[n - 1]:
            a[n], a[n - 1] = a[n - 1], a[n]

for i in range(ELEMENTS):
    print(a[i], end = "\t")