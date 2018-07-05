PEOPLE = 100

SSNs = [None] * PEOPLE
first_names = [None] * PEOPLE
last_names = [None] * PEOPLE

for i in range(PEOPLE):
    SSNs[i] = input("사회보장번호(SSN)를 입력하여라: ")
    first_names[i] = input("영문 이름을 입력하여라: ")
    last_names[i] = input("영문 성을 입력하여라: ")

needle = input("찾고자 하는 사회보장번호(SSN)를 입력하여라: ")

i = 0
while i < PEOPLE - 1 and SSNs[i] != needle:
    i += 1

if SSNs[i] != needle:
    print("아무것도 찾지 못하였습니다.")
else:
    print(first_names[i], last_names[i])