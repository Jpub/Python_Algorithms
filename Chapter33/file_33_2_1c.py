STUDENTS = 20
LESSONS = 10

grades = [ [None] * LESSONS for i in range(STUDENTS) ]

for i in range(STUDENTS):
    print("학생 번호:", (i + 1))
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + "번째 교과목의 점수를 입력하여라: "))

# 행 단위 평균을 계산한 후, 89점보다 높은 점수 직접 출력
for i in range(STUDENTS):
    average = 0
    for j in range(LESSONS):
        average += grades[i][j]
    average /= LESSONS
    if average > 89:
        print(average)
