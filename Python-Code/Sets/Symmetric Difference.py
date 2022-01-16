# Enter your code here. Read input from STDIN. Print output to STDOUT
M_size = input()
M = set(map(int, set(input().split())))
N_size = input()
N = set(map(int, set(input().split())))

M_difference = M.difference(N)
N_difference = N.difference(M)
combined_set = set.union(N_difference, M_difference)

for i in sorted(combined_set):
    print(int(i))
