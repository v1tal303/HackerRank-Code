# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
set_1 = set(input().split())
b = input()
set_2 = set(input().split())

print(len(set_1.union(set_2)))