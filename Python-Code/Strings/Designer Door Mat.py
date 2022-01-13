# Enter your code here. Read input from STDIN. Print output to STDOUT
values = input()
N = int(values.split(" ")[0])
M = N * 3
count = 1
middle = (N-1)/2


for i in range(0, N):
    if i < middle:
        mid = (".|."*count)
        dash = ("-"*int((M-(count*3))/2))
        count += 2
        print(dash+mid+dash)
    elif i == middle:
        mid_dash = ("-" * int((M-7)/2))
        count -= 2
        print(mid_dash + "WELCOME" + mid_dash)
    if i > middle:
        mid = (".|."*count)
        dash = ("-"*int((M-(count*3))/2))
        count -= 2
        print(dash+mid+dash)     
    
    