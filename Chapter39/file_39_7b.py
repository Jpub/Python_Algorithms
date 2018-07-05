def part1(i):
    while True:
        temp1 = input("성별을 입력하세요(" + str(i + 1) + "): ")
        sex = temp1.lower()
        if sex == "남자" or sex == "여자": break

    return sex

def part2():
    while True:
        temp2 = input("오후에 조깅을 하나요? ")
        answer = temp2.lower()
        if answer == "예" or answer == "아니요" or answer == "종종": break

    return answer

def part3(answer, sex, total_yes, female_no):
    if answer == "예":
        total_yes += 1

    if sex == "여자" and answer == "아니요":
        female_no += 1
        
    return total_yes, female_no

def part4(total_yes, female_no):
    print("긍적적인 답변의 수:", total_yes)
    print("여성의 부정적인 답변의 수:", female_no)

# 메인 코드
total_yes = 0
female_no = 0
for i in range(100):
    sex = part1(i)
    answer = part2()
    total_yes, female_no = part3(answer, sex, total_yes, female_no)

part4(total_yes, female_no)
