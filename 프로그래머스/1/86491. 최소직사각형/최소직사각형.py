def solution(sizes):
    max1 = 0
    max2 = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1] :
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    print(sizes)
    
    max1 = sizes[0][0]
    max2 = sizes[0][1]
    for j in sizes:
        if j[0] > max1 :
            max1 = j[0]
        
        if j[1] > max2:
            max2 = j[1]
            
    return max1 * max2