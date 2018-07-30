s = "I have a dream"

letter = input("검색할 영문자를 입력하여라: ")

found = False
for a in s:
    if a == letter:
        found = True
        break

if found == True:
    print("문자 ", letter, "를 찾았습니다.")