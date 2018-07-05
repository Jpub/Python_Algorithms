STUDENTS = 10
LESSONS = 5

# 리스트 names와 grades로 값을 입력받는다.
names = [None] * STUDENTS
grades = [ [None] * LESSONS for i in range(STUDENTS) ]

for i in range(STUDENTS):
    names[i] = input(str(i + 1) + "번째 학생의 이름을 입력하여라: ")
    for j in range(LESSONS):
        grades[i][j] = int(input(str(j + 1) + \
        "번째 과목의 성적을 입력하여라: "))

# 리스트 average를 생성한다.
average = [None] * STUDENTS
for i in range(STUDENTS):
    average[i] = 0
    for j in range(LESSONS):
        average[i] += grades[i][j]
    average[i] /= LESSONS

# 리스트 average와 names를 정렬한다.
for m in range(STUDENTS - 1):
    for n in range(STUDENTS - 1, m, -1):
        if average[n] > average[n - 1]:
            average[n], average[n - 1] = average[n - 1], average[n]
            names[n], names[n - 1] = names[n - 1], names[n]
        elif average[n] == average[n - 1]:
            if names[n] < names[n - 1]:
                names[n], names[n - 1] = names[n - 1], names[n]

# 리스트 names와 average를 출력한다.
for i in range(STUDENTS):
    print(names[i], "\t", average[i])