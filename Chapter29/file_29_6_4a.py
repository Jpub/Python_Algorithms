message = input("메시지를 입력하여라: ").lower()

# 공백, 쉼표, 구두점, 물음표를 제외한 모든 문자를 포함한 문자열을 생성
message_clean = ""
for letter in message:
    if letter != " " and letter != "," and letter != "." and letter != "?":
        message_clean += letter

# message_clean의 중간 위치
middle_pos = (len(message_clean) - 1) // 2

# message_clean의 마지막 위치
j = len(message_clean) - 1

# 우선, 문장이 회문이라고 가정
palindrome = True

# for-루프가 문자 하나씩 비교
for i in range(middle_pos + 1):
    left_letter = message_clean[i]
    right_letter = message_clean[j]
    # 적어도 문자 쌍 중에 어느 하나라도 검증에 실패한다면,
    # palindrome 변수를 False로 설정
    if left_letter != right_letter:
        palindrome = False
    j -= 1

# 변수 palindrome이 여전히 True이면
if palindrome == True:
    print("이 메시지는 회문입니다.")
