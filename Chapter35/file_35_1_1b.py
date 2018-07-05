import math
ELEMENTS_OF_A = 100

a = [None] * ELEMENTS_OF_A
for i in range(ELEMENTS_OF_A):
    a[i] = float(input())

new_arr = []
for i in range(ELEMENTS_OF_A - 2):
    new_arr.append(math.fsum(a[i:i + 3]) / 3)

for element in new_arr:
    print(element)