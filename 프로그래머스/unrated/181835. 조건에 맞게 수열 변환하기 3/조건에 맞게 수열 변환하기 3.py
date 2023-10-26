def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if k % 2 == 1:
            arr[i] = arr[i] * k
        else:
            arr[i] = arr[i] + k
    return arr