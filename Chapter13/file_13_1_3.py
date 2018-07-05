number = int(input("경과 시간(초)을 입력하여라: "))

days, r = divmod(number, 86400)   # 60 * 60 * 24 = 86400
hours, r = divmod(r, 3600)        # 60 * 60 = 3600
minutes, seconds = divmod(r, 60)

print(days, "일 ", hours, "시간 ")
print(minutes, "분 ", seconds, "초")
