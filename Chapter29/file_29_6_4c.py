message = input("메시지를 입력하여라: ").lower()

message_clean = ""
for letter in message:
    if letter not in " ,.?":
        message_clean += letter

middle_pos = (len(message_clean) - 1) // 2

palindrome = True
i = 0
while i <= middle_pos and palindrome == True:
    if message_clean[i] != message_clean[-i - 1]:
        palindrome = False
    i += 1

if palindrome == True:
    print("이 메시지는 회문입니다.")
