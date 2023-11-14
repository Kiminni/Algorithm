def solution(quiz):
    answer_list = []
    
    for quiz_query in quiz:
        quiz_query = quiz_query.split()
        answer = int(quiz_query[0])
        
        for i in range(len(quiz_query)):
            if quiz_query[i] == '+':
                answer += int(quiz_query[i+1])
            elif quiz_query[i] == '-':
                answer -= int(quiz_query[i+1])
        
        if int(quiz_query[-1]) == answer:
            answer_list.append('O')
        else:
            answer_list.append('X')
            
    return answer_list