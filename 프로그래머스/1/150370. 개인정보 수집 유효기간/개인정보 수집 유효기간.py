def solution(today, terms, privacies):
    answer = []
    dic = {}
    today_list = list(map(int, today.split('.'))) # 오늘 날짜 list로
    
    for term in terms: # 종류와 약관을 일 수로
        num1, num2 = term.split(" ")
        dic[num1] = int(num2) * 28 
    
    for i in range(len(privacies)): 
        d, s = privacies[i].split() #약관과 날짜로 분리
        date_list = list(map(int, d.split('.'))) #수집 일자 리스트로
        
        year = (today_list[0] - date_list[0]) * 336 # 연
        month = (today_list[1] - date_list[1]) * 28 # 월
        day = today_list[2] - date_list[2] # 일
        total = year + month + day
        
        if dic[s] <= total: # 다 더해서 보관 가능하면 추가
            answer.append(i+1)
            
    return answer
