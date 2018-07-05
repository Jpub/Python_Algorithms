import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

a = "753"
print(re.match(IS_NUMERIC, a))    # 출력: True

a = "-753.6"
print(re.match(IS_NUMERIC, a))    # 출력: True

a = "Hello"
print(re.match(IS_NUMERIC, a))    # 출력: False
