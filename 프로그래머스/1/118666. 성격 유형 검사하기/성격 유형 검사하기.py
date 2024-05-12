'''
딕셔너리? 혹은 리스트에 각각의 값을 저장 후 리턴하는 형식
'''
def solution(survey, choices):
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    score = [3,2,1,0,1,2,3]
    
    answer = ''
    for i in range(len(choices)):
        if choices[i] < 4:
            dic[survey[i][0]] += score[choices[i]-1]
        elif 4 < choices[i]:
            dic[survey[i][1]] += score[choices[i]-1]
            
    type = list(dic.keys())
    
    for j in range(0, len(dic), 2):
        if dic[type[j]] > dic[type[j+1]]:
            answer += type[j]
        elif dic[type[j]] < dic[type[j+1]]: 
            answer += type[j+1]
        else:
            answer += min(type[j], type[j+1])
    return answer