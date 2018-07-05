sentence = input("영어 문장을 입력하여라: ")

# 첫 번째 문자를 가져온다.
first_char = sentence[0]

# 마지막 문자를 가져온다.
last_char = sentence[-1]

sentence_is_okay = True

if first_char != first_char.upper():
    sentence_is_okay = False
elif last_char != "." and last_char != "?" and last_char != "!":
    sentence_is_okay = False

if sentence_is_okay == True:
    print("이상 없음!")
