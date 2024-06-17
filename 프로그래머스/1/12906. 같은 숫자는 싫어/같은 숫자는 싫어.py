def solution(arr):
    stack = [arr[0]]
    for i in range(len(arr)):
        if arr[i] == stack[-1]:
            continue
        else:
            stack.append(arr[i])
    return stack