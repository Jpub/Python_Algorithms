STUDENTS = 10
LESSONS = 5

grades = [ [None] * LESSONS for i in range(STUDENTS) ]

for i in range(STUDENTS):
    print("학생 번호:", (i + 1))
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + "번째 교과목의 " + \
        "점수를 입력하여라: "))

# 열 단위로 평균 점수를 계산한 후, 89점보다 높은 점수를 바로 출력
for j in range(LESSONS):
    average = 0
    for i in range(STUDENTS):
        average += grades[i][j]
    average /= STUDENTS
    if average > 89:
        print(average)
