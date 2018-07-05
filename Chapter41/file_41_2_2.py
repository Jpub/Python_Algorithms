PEOPLE = 20
 
def my_sort(a, ascending = True): 
    for m in range(PEOPLE - 1): 
        for n in range(PEOPLE - 1, m, -1): 
            if ascending == True: 
                if a[n] < a[n - 1]: 
                    a[n], a[n - 1] = a[n - 1], a[n] 
            else: 
                if a[n] > a[n - 1]: 
                    a[n], a[n - 1] = a[n - 1], a[n] 
                 
def display_list(a): 
    for i in range(PEOPLE): 
        print(a[i]) 
 
# 메인 코드
names = [None] * PEOPLE 
for i in range(PEOPLE): 
    names[i] = input("이름을 입력하여라: ") 
 
my_sort(names)          # 이름을 오름차순으로 정렬 
display_list(names)     # 정렬된 이름 출력
 
my_sort(names, False)   # 이름을 내람차순으로 정렬
display_list(names)     # 정렬된 이름 출력   