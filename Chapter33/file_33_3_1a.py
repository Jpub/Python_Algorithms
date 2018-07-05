STUDENTS = 10
LESSONS = 5

grades = [ [None] * LESSONS for i in range(STUDENTS) ]
for i in range(STUDENTS):
    print("학생 번호:", (i + 1))
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + "번째 교과목의 " + \
        "점수를 입력하여라: "))

# average 리스트를 생성한 후, 열 단위로 반복 처리 
average = [None] * LESSONS
for j in range(LESSONS):
    average[j] = 0
    for i in range(STUDENTS):
        average[j] += grades[i][j]
    average[j] /= STUDENTS

# 89점보다 높은 평균 점수 모두를 출력
for j in range(LESSONS):
    if average[j] > 89:
        print(average[j])
