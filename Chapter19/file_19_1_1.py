x = int(input())
y = 10

if x < 30:
    if x < 15:
        y = y + 2
    else:
        y -= 1
else:
    y += 1

print(y)
