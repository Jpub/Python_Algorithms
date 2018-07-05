def display_value():
    global test
    print(test)    # 10 출력
    test = 20
    print(test)    # 20 출력

# 메인 코드
test = 10
display_value()
print(test)        # 20 출력
