p = 1

a = float(input())
while True:
    p = p * a
    a = float(input())
    if a == -1: break

print(p)
