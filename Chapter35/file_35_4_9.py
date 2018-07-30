months = ["1월", "2월", "3월", "4월", "5월", "6월", \
          "7월", "8월", "9월", "10월", "11월", "12월"]

kwh = [None] * len(months)

for i in range(len(months)):
    kwh[i] = float(input(months[i] + "의 kWh를 입력하여라: "))

for m in range(len(months)):
    maximum = kwh[m]
    index_of_max = m
    for n in range(m, len(months)):
        if kwh[n] > maximum:
            maximum = kwh[n]
            index_of_max = n

    # kwh 내 두 요소 위치의 값을 맞바꾼다.
    kwh[m], kwh[index_of_max] = kwh[index_of_max], kwh[m]
    # months 내 두 요소 위치의 값을 맞바꾼다.
    months[m], months[index_of_max] = months[index_of_max], months[m]

for i in range(len(months)):
    print(months[i], ":", kwh[i])