total_yes = 0
female_no = 0
for i in range(100):

    while True:
        temp1 = input("성별을 입력하세요(" + str(i + 1) + "): ")
        sex = temp1.lower() # 영어 입력일 경우 소문자로 변경
        if sex == "남자" or sex == "여자": break

    while True:
        temp2 = input("오후에 조깅을 하나요? ")
        answer = temp2.lower() # 영어 입력일 경우 소문자로 변경
        if answer == "예" or answer == "아니요" or answer == "종종": break

    if answer == "예":
        total_yes += 1

    if sex == "여자" and answer == "아니요":
        female_no += 1

print("긍정적인 답볍의 수:", total_yes)
print("여성의 부정적인 답변의 수:", female_no)
