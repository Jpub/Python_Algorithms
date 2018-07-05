def prepend_title(first_name, last_name, title = "Mr.", reverse = False):
    if reverse == False:
        return_value = title + " " + first_name + " " + last_name
    else:
        return_value = title + " " + last_name + " " + first_name
    return return_value

# 메인 코드

# Mr. John King 출력
print(prepend_title("John", "King"))

# Ms. Maria Miller 출력
print(prepend_title("Maria", "Miller", "Ms."))

# Ms. Miller Maria 출력
print(prepend_title("Maria", "Miller", "Ms.", True))

# ㅋ키워드 인자를 사용하여 Mr. King John 출력
print(prepend_title("John", "King", reverse = True))
