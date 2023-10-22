def solution(rank, attendance):
    answer = 0
    grade = []
    for i in range(len(rank)):
        if attendance[i] == True:
            grade.append([i,rank[i]])

    grade.sort(key = lambda x: x[1])
    print(grade)
    return 10000 * grade[0][0] + 100 * grade[1][0] + grade[2][0]