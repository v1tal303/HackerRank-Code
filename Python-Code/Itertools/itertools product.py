# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = map(int,input().split())
b = map(int,input().split())

prod = product(a,b)
print(*list(prod))