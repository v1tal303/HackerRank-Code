if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
def find_avg(name):
    avg_score = format(sum(student_marks[name]) / len(student_marks[name]), '.2f')
    return avg_score
    
print(find_avg(query_name))