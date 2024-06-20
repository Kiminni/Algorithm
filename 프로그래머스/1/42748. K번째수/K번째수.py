def solution(array, commands):
    answer = []
    for c in commands:
        c[0], c[1], c[2] = c[0] - 1, c[1] - 1, c[2] - 1
        arr = array[c[0] : c[1] + 1]
        arr = sorted(arr)
        answer.append(arr[c[2]])
    return answer