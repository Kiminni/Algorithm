def solution(genres, plays):
    answer = []
    tmp = []
    dic_genre = {genre : [] for genre in genres}
    dic_sum = {genre : 0 for genre in genres}
    
    for i in range(len(genres)):
        dic_genre[genres[i]] += [[i, plays[i]]]
        dic_sum[genres[i]] += plays[i]

    dic_sum = sorted(dic_sum.items(), key = lambda x : x[1], reverse = True)

    
    for dic in dic_sum:
        tmp.append(dic[0])

    
    for d in tmp:
        dic_genre[d] = sorted(dic_genre[d], key = lambda x: -x[1])
        
        for i in range(len(dic_genre[d])) :
            if i < 2:
                answer.append(dic_genre[d][i][0])
    
    
    return answer
        
        
    
        
    