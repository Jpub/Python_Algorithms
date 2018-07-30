def prepend_title(name, title = "Mr."):
    return title + " " + name

# 메인 코드

# Mr. John King 출력
print(prepend_title("John King"))

# Ms. Maria Miller 출력
print(prepend_title("Maria Miller", "Ms."))