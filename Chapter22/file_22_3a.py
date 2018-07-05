print("네 사람의 몸무게를 입력하여라:")

w1 = int(input())
w2 = int(input())
w3 = int(input())
w4 = int(input())


# 첫 번째 사람의 몸무게를 저장
minimum = w1

# 두 번째 사람의 몸무게가 첫 번째 사람보다 적게 나가면
# 두 번째 사람의 몸무게를 저장
if w2 < minimum:
    minimum = w2

# 세 번째 사람의 몸무게가 minimum보다 적으면
# 세 번째 사람의 몸무게를 저장
if w3 < minimum:
    minimum = w3

# 네 번째 사람의 몸무게가 minimum보다 적으면
# 네 번째 사람의 몸무게를 저장
if w4 < minimum:
    minimum = w4

print(minimum)
