count = 0

total = 0            # total 변수의 초기화
while total <= 1000:
    x = float(input())
    count += 1
    total += x        # total 변수의 갱신/변경

print(count)
