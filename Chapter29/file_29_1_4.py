N = int(input())
s = 0
for i in range(3, 3 * N + 3, 3):
    s = s + i ** i

print(s)
