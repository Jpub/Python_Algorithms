maximum = -1
count = 0

for i in range(20):
    while True:
        grade = int(input("학생 번호 " + str(i + 1) + "의 점수을 입력하여라: "))
        if 0 <= grade <= 100: break

    if grade > maximum:
        maximum = grade

    if grade >= 90:
        count += 1

print(maximum, count)
