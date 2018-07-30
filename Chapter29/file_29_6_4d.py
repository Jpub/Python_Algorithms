message = input("메시지를 입력하여라: ").lower()

# 공백, 쉼표, 구두점, 물음표를 제외한 모든 문자를 포함하고 있는 
# 새로운 문자열을 생성
message_clean = message
for c in " ,.?":
    message_clean = message_clean.replace(c, "")

if message_clean == message_clean[::-1]:
    print("이 메시지는 회문입니다.")
