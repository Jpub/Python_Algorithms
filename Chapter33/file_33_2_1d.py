import math

STUDENTS = 20
LESSONS = 10

grades = [ [None] * LESSONS for i in range(STUDENTS) ]

for i in range(STUDENTS):
    print("학생 번호:", (i + 1))
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + "번째 교과목의 " + \
        "점수를 입력하여라: "))

# 파이썬만의 강력한 기능을 사용하여 행 단위 평균 계산
for row in grades:
    average = math.fsum(row) / LESSONS
    if average > 89:
        print(average)
