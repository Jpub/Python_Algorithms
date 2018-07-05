n = int(input())

p = 1

i = 1
if i <= n:
    while True:
        a = float(input())
        p = p * a

        i += 1
        if i > n: break

print(p)
