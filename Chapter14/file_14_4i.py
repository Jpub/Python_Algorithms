import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

a = "753"
print(re.match(IS_NUMERIC, a))    # True로 간주됨.

a = "-753.6"
print(re.match(IS_NUMERIC, a))    # True로 간주됨.

a = "Hello"
print(re.match(IS_NUMERIC, a))    # False로 간주됨.
