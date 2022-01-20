# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
sample = input()
s = sorted(sample.split()[0])
iterations = int(sample.split()[1])

for i in range(1, iterations+1):
    perm = list(combinations(s, i))
    for x in perm:
        print("".join(x))