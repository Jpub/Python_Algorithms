import re

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"
STUDENTS = 100

names = [None] * STUDENTS
grades = [None] * STUDENTS
for i in range(STUDENTS):
    names[i] = input(str(i + 1) + "번째 학생 이름을 입력하여라: ")

    inp = input("점수를 입력하여라: ")
    while not re.match(IS_NUMERIC, inp) or int(inp) < 0:
        print("부적절한 값입니다.")
        inp = input("점수를 입력하여라: ")
    grades[i] = int(inp)

maximum = grades[0]             # 혹은 다음과 같이 해결할 수도 있음.
for i in range(1, STUDENTS):    # maximum = max(grades)
    if grades[i] > maximum: 
        maximum = grades[i] 

print("가장 높은 점수를 가진 학생:")
for i in range(STUDENTS):
    if grades[i] == maximum:
        print(names[i])
