from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    r = list(set(report))
    u = defaultdict(set) # 신고한 id
    r_ed = defaultdict(int) # 신고당한 횟수
    
    for data in r:
        n1, n2 = data.split(" ")
        u[n1].add(n2) # n1 -> n2 신고 {n1, n2} 식으로 저장
        r_ed[n2] += 1
    
    for i in id_list: # 전체 id에서 검색
        result = 0 
        for j in u[i]: #u[i]라는 딕셔너리에서 j의 값을 검색
            if r_ed[j] >= k: #r_ed가 k보다 크면 += 1
                result += 1
        answer.append(result)
    
    return answer