def solution(arr1, arr2):
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
    answer = []
    for i in range(m):
        arr = arr1[i]
        result = []
        for j in range(r):
            tmp = 0
            for k in range(n):
                tmp += arr[k] * arr2[k][j]
            result.append(tmp)
        answer.append(result)
    
    return answer
            

