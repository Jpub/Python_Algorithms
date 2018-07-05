message = input("메시지를 입력하여라: ").lower()

# "not in" 멤버십 연산자를 사용하여 공백, 쉼표, 구두점, 물음표를 제거
message_clean = ""
for letter in message:
    if letter not in " ,.?":
        message_clean += letter

middle_pos = (len(message_clean) - 1) // 2

palindrome = True

for i in range(middle_pos + 1):
    left_letter = message_clean[i]
    # 음수 인덱스를 사용하여 문자를 오른쪽에서부터 접근
    right_letter = message_clean[-i - 1]
    if left_letter != right_letter:
        palindrome = False
        break

if palindrome == True:
    print("이 메시지는 회문입니다.")
