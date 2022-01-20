# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
sample = input()
s = sorted(sample.split()[0])
iterations = int(sample.split()[1])


perm = list(combinations_with_replacement(s, iterations))
for x in perm:
    print("".join(x))