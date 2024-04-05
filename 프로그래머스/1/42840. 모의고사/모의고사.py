def solution(answers):
    answer = []
    answer1 = [1,2,3,4,5] * 2000
    answer2 = [2,1,2,3,2,4,2,5] * 1250
    answer3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    tmp1 = tmp2 = tmp3 = 0
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            tmp1 += 1
        if answers[i] == answer2[i]:
            tmp2 += 1
        if answers[i] == answer3[i]:
            tmp3 += 1
    max_ans = max(tmp1, tmp2, tmp3)
    if tmp1 == max_ans:
        answer.append(1)
    if tmp2 == max_ans:
        answer.append(2)
    if tmp3 == max_ans:
        answer.append(3)
    return answer
