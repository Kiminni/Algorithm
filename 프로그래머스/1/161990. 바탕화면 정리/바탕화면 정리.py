def solution(wallpaper):
    wal_num = [[]]
    lux, luy, rdx, rdy = 51, 51, 0, 0
    answer = []
    tmp= []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                tmp.append([i,j])
    
    for t in range(len(tmp)):
        if tmp[t][0] < lux :
            lux = tmp[t][0]
        if tmp[t][1] < luy:
            luy = tmp[t][1]
        if tmp[t][0] > rdx:
            rdx = tmp[t][0]
        if tmp[t][1] > rdy:
            rdy = tmp[t][1]
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx + 1)        
    answer.append(rdy + 1)
    return answer