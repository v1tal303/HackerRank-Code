if __name__ == '__main__':
    N = int(input())
    a_list = []
    for i in range(0, N):
        input_str = input()
        l = input_str.split()
        if l[0] == 'insert':
            a_list.insert(int(l[1]), int(l[2]))
        elif l[0] == 'print':
            print(a_list)
        elif l[0] == 'remove':
            a_list.remove(int(l[1]))
        elif l[0] == 'append':
            a_list.append(int(l[1]))
        elif l[0] == 'sort':
            a_list.sort()
        elif l[0] == 'pop':
            a_list.pop()
        elif l[0] == 'reverse':
            a_list.reverse()