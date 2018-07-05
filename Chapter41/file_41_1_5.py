import random
ELEMENTS = 100

def dice():
    return random.randrange(1, 7)

def search_and_count(x, a):
    count = 0

    for i in range(ELEMENTS):
        if a[i] == x:
            count += 1
    return count

# 메인 코드

# 1과 6 사이의 무작위 수를 가진 리스트 a 생성
a = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = dice()

# 리스트 n을 생성하고, 리스트 a에 주사위의 각 숫자가 몇 번 나왔는지를 출력
n = [None] * 6
for i in range(6):
    n[i] = search_and_count(i + 1, a)
    print("Value", (i + 1), "appears", n[i], "times")

# 리스트 n에서 최댓값 찾기
maximum = n[0]
max_i = 0
for i in range(1, 6):
    if n[i] > maximum:
        maximum = n[i]
        max_i = i

# 리스트 n에서 가장 많이 나온 숫자를 출력
print((max_i + 1), "이(가) 리스트에서 가장 많이 나옴:", maximum, "번")
