def solution(s, n):
    answer = []
    for i in range(len(s)):

        n %= 26
        
        tmp = ord(s[i]) + n
    
        if s[i] == ' ':
            answer.append(' ')
            continue
        
        if ord('Z') < tmp :
            if 'A' <= s[i] <= 'Z': 
                answer.append(chr(tmp - ord('Z') + ord('A') - 1))
                continue

        if tmp > ord('z'):
            answer.append(chr(tmp - ord('z') + ord('a') - 1))
            continue
        

        
        answer.append(chr(tmp))
    return ''.join(answer)
    