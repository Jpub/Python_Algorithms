STUDENTS = 10
LESSONS = 5

# 이름과 점수를 함께 입력받음
names = [None] * STUDENTS
grades = [ [None] * STUDENTS for i in range(LESSONS) ]
for j in range(STUDENTS):
    names[j] = input(str(j + 1) + "번째 학생의 이름을 입력하여라: ")
    for i in range(LESSONS):
        grades[i][j] = int(input(str(names[j]) + " 학생의 " + \
                        str(i + 1) + "번째 과목 점수를 입력하여라: "))

# count 리스트 생성
count = [None] * STUDENTS
for j in range(STUDENTS):
    count[j] = 0
    for i in range(LESSONS):
        if grades[i][j] > 89:
            count[j] += 1

# 점수가 89점 이상인 학생 이름 출력
for j in range(STUDENTS):
    if count[j] > 1:
        print(names[j])