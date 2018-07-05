s = 0
count = 0
for i in range(100):
    x = float(input())
    if x > 0:
        s = s + x
        count += 1

if count != 0:
    print(s / count)
else:
    print("숫자가 입력되지 않습니다!")
