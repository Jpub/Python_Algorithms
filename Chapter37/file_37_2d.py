def get_fullname():
    first_name = input("영문 성을 입력하여라: ")
    last_name = input("영문 이름을 입력하여라: ")
    return first_name, last_name

# 메인 코드가 여기서 시작된다.
fname, lname = get_fullname()
print("영문 성:", fname)
print("영문 이름:", lname)
