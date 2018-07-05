ELEMENTS = 100

a = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = int(input())

b = []
for element in a:
    first_digit, last_digit = divmod(element, 10)
    if 5 in [first_digit, last_digit]:
        b.append(element)

for element in b:
    print(element, end = "\t")