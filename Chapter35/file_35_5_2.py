PEOPLE = 20

first_names = [None] * PEOPLE
last_names = [None] * PEOPLE

for i in range(PEOPLE):
    first_names[i] = input("영문 이름을 입력하여라: ")
    last_names[i] = input("영문 성을 입력하여라: ")

needle = input("검색하고자 하는 영문 이름을 입력하여라: ")

found = False
for i in range(PEOPLE):
    if first_names[i].upper() == needle.upper():
        print(last_names[i])
        found = True

if found == False:
    print("어떤 사람도 발견하지 못하였습니다.")