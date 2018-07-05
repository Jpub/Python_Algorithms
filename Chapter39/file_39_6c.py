def display_value():
    print(test)    # 이 명령문에서 오류가 발생한다.
    test = 20
    print(test)

# 메인 코드
test = 10
display_value()
print(test)
