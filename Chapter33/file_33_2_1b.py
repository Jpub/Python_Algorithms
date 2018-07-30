import math

STUDENTS = 20
LESSONS = 10

grades = [ [None] * LESSONS for i in range(STUDENTS) ]

for i in range(STUDENTS):
    print("학생 번호:", (i + 1))
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + "번째 교과목의 점수를 입력하여라: "))

# average 리스트 생성
average = []
for row in grades:
    average.append(math.fsum(row) / LESSONS)

# 89점보다 높은 점수 출력
for i in range(STUDENTS):
    if average[i] > 89:
        print(average[i])
