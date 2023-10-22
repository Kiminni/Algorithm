def solution(strArr):
    answer = 0
    count_list = [0]*31
    for i in range(len(strArr)):
        strArr[i] = "a" * len(strArr[i])
    strArr.sort()
    for idx in range(len(strArr)):
        count_list[len(strArr[idx])] += 1
    print(count_list)
    return max(count_list)