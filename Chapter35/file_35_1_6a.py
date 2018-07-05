ELEMENTS = 100

a = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = int(input())

b = [None] * ELEMENTS
k = 0
for i in range(ELEMENTS):
    last_digit = a[i] % 10
    first_digit = a[i] // 10
    
    if first_digit == 5 or last_digit == 5:
        b[k] = a[i]
        k += 1
        
for i in range(k):
    print(b[i], end = "\t")