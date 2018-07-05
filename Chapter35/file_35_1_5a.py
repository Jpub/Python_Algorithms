ELEMENTS = 100

ar = [None] * ELEMENTS
for i in range(ELEMENTS):
    ar[i] = float(input())

# 리스트 pos와 neg를 생성한다.
pos = [None] * ELEMENTS
neg = [None] * ELEMENTS
pos_index = 0
neg_index = 0
for i in range(ELEMENTS):
    if ar[i] > 0:
        pos[pos_index] = ar[i]
        pos_index += 1
    elif ar[i] < 0:
        neg[neg_index] = ar[i]
        neg_index += 1
        
for i in range(pos_index):
    print(pos[i], end = "\t")

print()

for i in range(neg_index):
    print(neg[i], end = "\t")