def solution(s):
    answer = []
    num_dict = {
       "zero" : 0, 
       "one" : 1,
       "two" : 2, 
       "three" : 3, 
       "four" : 4, 
       "five" : 5, 
       "six" : 6,
       "seven" : 7,
       "eight" : 8,
       "nine" : 9
    }
    tmp = []
    for i in range(len(s)):
        if "0" <= s[i] <= '9':
            answer.append(s[i])
        
        else:
            tmp.append(s[i])
            if ''.join(tmp) in num_dict:
                answer.append(str(num_dict[''.join(tmp)]))
                tmp = []
    
    return int(''.join(answer))
    