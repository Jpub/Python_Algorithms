N = int(input())
s = 0
for i in range(2, 2 * N + 2, 2):
    s = s + i ** 2

print(s)
