w1 = int(input("첫 번째 사람의 몸무게를 입력하여라: "))
n1 = input("첫 번째 사람의 이름을 입력하여라: ")

w2 = int(input("두 번째 사람의 몸무게를 입력하여라: "))
n2 = input("두 번째 사람의 이름을 입력하여라: ")

w3 = int(input("세 번째 사람의 몸무게를 입력하여라: "))
n3 = input("세 번째 사람의 이름을 입력하여라: ")

maximum = w1
m_name = n1            # 몸무게가 가장 많이 나가는 사람의 이름을 저장할 변수

if w2 > maximum:
    maximum = w2
    m_name = n2    # maximum보다 w2가 크므로 n2값을 m_name에 저장

if w3 > maximum:
    maximum = w3
    m_name = n3    # maximum보다 w3가 크므로 n3값을 m_name에 저장

print("몸무게가 가장 많이 나가는 사람:", m_name)
print("몸무게:", maximum)
