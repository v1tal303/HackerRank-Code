import re
for i in range(int(input())):
    a = True
    try:
        reg = re.compile(input())
    except re.error:
        a = False
    print(a)