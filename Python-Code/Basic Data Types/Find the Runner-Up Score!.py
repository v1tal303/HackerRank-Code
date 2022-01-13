if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
new_list = list(set(arr))

print(sorted(new_list)[-2])