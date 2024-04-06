def solution(number, limit, power):
    answer = []
    for idx in range(1, number + 1):
        tmp = 0
        for i in range(1, int(idx**(1/2)) + 1):
            if idx % i == 0 :
                tmp += 1
                if i **2 != idx:
                    tmp += 1
            if tmp > limit:
                tmp = power
                break
        answer.append(tmp)
    return sum(answer)

