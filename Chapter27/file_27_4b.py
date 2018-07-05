s = "I have a dream"

letter = input("검색할 영문자를 입력하여라: ")

found = False
i = 0
while i <= len(s) - 1 and found == False:
    if s[i] == letter:
        found = True
    i += 1

if found == True:
    print("문자", letter, "를 찾았습니다.")
