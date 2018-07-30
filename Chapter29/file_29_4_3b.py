m1 = int(input())
m2 = int(input())

s = 0
while m2 != 0:
    if m2 % 2 != 0:
        s += m1

    m1 = m1 << 1    # m1 *= 2와 동일
                    # m1의 비트들을 왼쪽으로 한 번의 시프트
    m2 = m2 >> 1    # m2 //= 2와 동일
                    # m2의 비트들을 오른쪽으로 한 번의 시프트
print(s)
