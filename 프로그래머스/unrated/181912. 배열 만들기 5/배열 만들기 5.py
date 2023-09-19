def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        string = ''
        for i in range(s, s + l):
            string += num[i]
        if int(string) > k:
            answer.append(int(string))
            
        
    return answer