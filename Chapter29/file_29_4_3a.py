m1 = int(input())
m2 = int(input())
s = 0
while m2 != 0:
    if m2 % 2 != 0:
        s += m1
        
    m1 *= 2
    m2 //= 2

print(s)
