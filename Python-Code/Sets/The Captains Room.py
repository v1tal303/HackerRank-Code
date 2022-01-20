# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

A = int(input())
room_num = input().split()

test = Counter(room_num)

for key, value in test.items():
    if 1 == value:
        print(key)
