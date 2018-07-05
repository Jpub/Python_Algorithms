full_name = input("당신의 영문 이름을 입력하여라: ")

# 스페이스 문자의 위치를 찾는다. 또한, 이름에 포함된 문자 개수를 나타낸다.
space_pos = full_name.find(" ")

# 위치 0에서 space_pos 문자 개수만큼의 부분 문자열을 얻는다.
name1 = full_name[:space_pos]

# 위치 space_pos + 1에서 마지막까지의 부분 문자열을 얻는다.
name2 = full_name[space_pos + 1:]

full_name = name2 + " " + name1
print(full_name)
