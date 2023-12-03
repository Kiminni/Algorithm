def solution(A, B):
    answer = -1
    
    if len(A) != len(B):
        return answer
    for i in range(len(A)):
        print(A[-1])
        if A == B: 
            return i 
        last_char = A[-1]
        A = last_char + A[:-1]
        print(A)
    if A == B:
        return 0
    return answer