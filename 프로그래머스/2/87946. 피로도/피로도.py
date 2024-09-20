def solution(k, dungeons):
    n = len(dungeons)
    picked = [False] * n

    def recur(cur_k, num):
        max_answer = num

        for i in range(n):
            if not picked[i] and cur_k >= dungeons[i][0]:
                picked[i] = True
                current = recur(cur_k - dungeons[i][1], num + 1)
                max_answer = max(max_answer, current)
                picked[i] = False

        return max_answer

    return recur(k, 0)