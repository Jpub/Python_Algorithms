v = input().upper()

if v == "M":                    #대문자 M으로만 검사
    print("1000원을 지불해야 합니다.")
elif v == "C":                  #대문자 C으로만 검사
    print("2000원을 지불해야 합니다.")
elif v == "T":                  #대문자 T으로만 검사
    print("4000원을 지불해야 합니다.")
else:
    print("차량 정보가 올바르지 않습니다.")
