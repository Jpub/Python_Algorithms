ROWS = 20
COLUMNS = 30

haystack = [ [None] * COLUMNS for i in range(ROWS) ]

for i in range(ROWS):
    for j in range(COLUMNS):
        haystack[i][j] = float(input())

needle = float(input("검색 값을 입력하여라: "))

count = 0
for j in range(COLUMNS):
    found = False
    for i in range(ROWS):
        if haystack[i][j] == needle:
            found = True
            break
            
    if found == True:
        count += 1
    else:
        break
    
if count == COLUMNS:
    print(needle, "이/가 모든 열에 있습니다.")
