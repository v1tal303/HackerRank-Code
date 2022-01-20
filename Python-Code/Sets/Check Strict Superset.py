# Enter your code here. Read input from STDIN. Print output to STDOUT
A_set = set(input().split())
n = int(input())
test = True

for i in range(n):
    B_set = set(input().split())
    if not B_set.issubset(A_set):
        test = False
    if len(B_set) >= len(A_set):
        test = False
print(test)