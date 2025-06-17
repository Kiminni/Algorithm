def solution(record):
    answer = []
    dic = {}
    command = []
    for r in record:
        r_list = r.split(" ")
        if r_list[0] == "Enter":
            dic[r_list[1]] = r_list[2]
            
        elif r_list[0] == "Change":
            dic[r_list[1]] = r_list[2]
        
        command.append((r_list[0], r_list[1]))
    
    for c in command:
        if c[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(dic[c[1]]))
        
        elif c[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(dic[c[1]]))
        
    
    return answer