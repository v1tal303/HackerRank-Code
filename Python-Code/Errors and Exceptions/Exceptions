# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    a = input().split()
    try:
        print(int(int(a[0])/int(a[1])))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)