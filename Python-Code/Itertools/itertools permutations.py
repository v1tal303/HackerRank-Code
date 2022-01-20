# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
sample = input()
s = sample.split()[0]
iterations = int(sample.split()[1])
perm = sorted(list(permutations(s, iterations)))


for i in perm:
    print("".join(i))