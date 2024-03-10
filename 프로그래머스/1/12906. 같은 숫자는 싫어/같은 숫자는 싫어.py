def solution(arr):
#     answer = [arr[0]]
#     for i in range(1, len(arr)):
#         if arr[i-1] != arr[i]:
#             answer.append(arr[i])
#     return answer

    c_arr = []
    c_arr.append(arr[0])
    m_arr = arr

    for i in m_arr:
        if i != c_arr[-1]:
            c_arr.append(i)
    return c_arr