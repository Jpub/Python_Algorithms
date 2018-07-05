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
a = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = dice()

x = int(input())
print("입력한 정수가 리스트에", search_and_count(x, a), "번 나왔습니다.")
