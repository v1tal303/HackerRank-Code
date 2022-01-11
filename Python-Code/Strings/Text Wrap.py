import textwrap

def wrap(string, max_width):
    string_list = [print(string[i:i+max_width]) for i in range(0, len(string), max_width)]
    return ""

if __name__ == '__main__':