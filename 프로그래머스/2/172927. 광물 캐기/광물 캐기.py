def solution(picks, minerals):
    answer = 0
    pick_sum = 0
    min_sum = 0
    pick_sum = sum(picks)
    
    #곡괭이로 캘 수 있는 광물만큼 자른다.
    min_sum = pick_sum * 5
    minerals = minerals[:min_sum]
    
    # 광물들을 조사한다.
    new_minerals =[[0,0,0] for _ in range((len(minerals) //5 + 1))]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1
        elif minerals[i]=='iron':
            new_minerals[i//5][1]+=1
        elif minerals[i]=='stone':
            new_minerals[i//5][2]+=1
    
    #광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in new_minerals:
        diamond,iron,stone = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += diamond + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * diamond) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * diamond) + (5 * iron) + stone
                break

    return answer