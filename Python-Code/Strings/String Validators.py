if __name__ == '__main__':
    s = input()

    list_of_checks = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    
    for i in list_of_checks:
        if any(map(i, s)):
            print(True)
        else:
            print(False)
