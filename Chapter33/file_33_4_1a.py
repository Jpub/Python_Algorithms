STUDENTS = 10
LESSONS = 5

names = [None] * STUDENTS
grades = [[None] * LESSONS for i in range(STUDENTS)]

# 학생의 이름과 성적을 함께 입력받음
for i in range(STUDENTS):
    names[i] = input(str(i + 1) + "번째 학생의 이름을 입력하여라: ")
    for j in range(LESSONS):
        grades[i][j] = int(input(str(names[i]) + " 학생의 " + \
        str(j + 1) + "번째 과목 점수를 입력하여라: "))

# count 리스트 생성
count = [None] * STUDENTS
for i in range(STUDENTS):
    count[i] = 0
    for j in range(LESSONS):
        if grades[i][j] > 89:
            count[i] += 1
# 점수가 89점 이상인 학생 이름 출력
for i in range(STUDENTS):
    if count[i] > 1:
        print(names[i])
