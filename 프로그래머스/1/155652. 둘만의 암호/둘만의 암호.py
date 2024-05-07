import string

def solution(s, skip, index):
    answer = []
    alpha = list(string.ascii_lowercase)
    
    for i in skip:
        if i in alpha:
            alpha.remove(i)
    for j in range(len(s)):
        print(answer)
        j_idx = alpha.index(s[j])
        answer.append(alpha[(j_idx + index)% len(alpha)])
    return ''.join(answer)
    

        