# Enter your code here. Read input from STDIN. Print output to STDOUT
A = input()
set_1 = set(input().split())


for i in range(int(input())):
    command = input().split()[0]
    set_x = set(input().split())
    eval("set_1.{0}({1})".format(command,set_x))
print(sum(map(int,set_1)))

