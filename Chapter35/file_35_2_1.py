ELEMENTS = 20

odds = [None] * ELEMENTS
for i in range(ELEMENTS):
    while True:
        odds[i] = int(input("홀수인 정수를 입력하여라: "))
        if odds[i] % 2 != 0: break

# 요소를 역순으로 출력                    # 또는 다음과 같이 변형 가능
for i in range(ELEMENTS - 1, -1, -1):   # for element in odds[::-1]:
    print(odds[i], end = "\t")          #     print(element, end = "\t")
