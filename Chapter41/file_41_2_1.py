import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"
PEOPLE = 5

def get_age():
    inp = input("나이를 입력하여라: ")
    while not re.match(IS_NUMERIC, inp) or int(inp) <= 0:
        print("오류: 올바르지 않은 나이값입니다.")
        inp = input("양수를 입력하여라: ")
    return int(inp)

def find_max(a):
    maximum = a[0]
    max_i = 0
    for i in range(1, PEOPLE):
        if a[i] > maximum:
            maximum = a[i]
            max_i = i
    return max_i

# 메인 코드
first_names = [None] * PEOPLE
last_names = [None] * PEOPLE
ages = [None] * PEOPLE

for i in range(PEOPLE):
    first_names[i] = input("영문 성을 입력하여라(" + str(i + 1) + "): ")
    last_names[i] = input("영문 이름을 입력하여라(" + str(i + 1) + "): ")
    ages[i] = get_age()

index_of_max = find_max(ages)

print("나이가 가장 많은 사람:", last_names[index_of_max], first_names[index_of_max])
print("나이가 가장 많은 사람의 나이는", ages[index_of_max], "세 입니다.")
