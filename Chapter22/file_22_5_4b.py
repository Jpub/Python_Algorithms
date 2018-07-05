sentence = input("영어 문장을 입력하여라: ")

if sentence[0] == sentence[0].upper() and sentence[-1] in ".?!":
    print("이상 없음!")
