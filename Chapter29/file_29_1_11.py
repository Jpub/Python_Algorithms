x = int(input())
s = 0

while x != 0:
    digit = x % 10      # x MOD 10 연산
    s = s + digit
    x = x // 10         # x DIV 10 연산

print(s)
