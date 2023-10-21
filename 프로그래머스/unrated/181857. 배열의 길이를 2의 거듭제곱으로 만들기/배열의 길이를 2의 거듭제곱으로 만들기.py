def solution(arr):
    count = 0
    length = len(arr)
    while length > 1:
        length /= 2
        count += 1 
    arr.extend([0] * (2 ** count - len(arr)))
    return arr 