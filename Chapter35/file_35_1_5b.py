ELEMENTS = 100
ar = [None] * ELEMENTS
for i in range(ELEMENTS):
    ar[i] = float(input())

# 리스트 pos와 neg를 생성한다.
pos = []
neg = []
for element in ar:
    if element > 0:
        pos.append(element)
    elif element < 0:
        neg.append(element)

for element in pos:
    print(element, end = "\t")

print()

for element in neg:
    print(element, end = "\t")