def display(color, exists):
    neg = "이 있다."
    if exists == False:
        neg = "은 없다."

    return "무지기에 " + color + neg

# 메인 코드가 여기서 시작된다.
print(display("빨간색", True))
print(display("노란색", True))
print(display("검은색", False))
