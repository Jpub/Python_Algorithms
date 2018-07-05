ELEMENTS = 10

def display(b):
    for i in range(ELEMENTS):
        print(b[i], end = "\t")

# 메인 코드
a = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = int(input())

display(a)
