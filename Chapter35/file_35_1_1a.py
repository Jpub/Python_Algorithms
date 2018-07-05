ELEMENTS_OF_A = 100
ELEMENTS_OF_NEW = ELEMENTS_OF_A - 2 

a = [None] * ELEMENTS_OF_A
for i in range(ELEMENTS_OF_A):
    a[i] = float(input())

new_arr = [None] * ELEMENTS_OF_NEW
for i in range(ELEMENTS_OF_NEW):
    new_arr[i] = (a[i] + a[i + 1] + a[i + 2]) / 3

for i in range(ELEMENTS_OF_NEW):
    print(new_arr[i])