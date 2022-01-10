if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        records.append(student)
        
sorted_records = sorted(records, key = lambda x: x[1])
second_lowest = sorted(list(set([x[1] for x in sorted_records])))[1]

names = []
for i in sorted_records:
    if i[1] == second_lowest:
        names.append(i[0])

for i in sorted(names):
    print(i)