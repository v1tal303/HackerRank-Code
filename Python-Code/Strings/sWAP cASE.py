def swap_case(s):
    reversed_str = []
    for i in s:
        if i.islower():
            reversed_str.append(i.upper())
        elif i.isupper():
            reversed_str.append(i.lower())
        else:
            reversed_str.append(i)
    final_reversed = ''.join(reversed_str)
    return final_reversed

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)