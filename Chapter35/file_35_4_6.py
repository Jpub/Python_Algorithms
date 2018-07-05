ELEMENTS = 20

w = [None] * ELEMENTS

for i in range(ELEMENTS):
    w[i] = float(input())

for m in range(ELEMENTS-1):
    swaps = False
    for n in range(ELEMENTS-1, m, -1):
        if w[n] < w[n-1]:
            w[n], w[n-1] = w[n-1], w[n]
            swaps = True
    if swaps == False: break

print("가장 무거운 몸무게:")
print(w[ELEMENTS-3])
print(w[ELEMENTS-2])
print(w[ELEMENTS-1])

print("가장 가벼운 몸무게:")
print(w[0])
print(w[1])
print(w[2])