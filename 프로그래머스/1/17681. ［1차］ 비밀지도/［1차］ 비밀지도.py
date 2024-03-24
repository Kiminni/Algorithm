def solution(n, arr1, arr2):
    answer = []
    tmp1 = []
    tmp2 = []
    for i in range(n):
        tmp1.append(bin(arr1[i])[2:])
        tmp2.append(bin(arr2[i])[2:])
        tmp1[i] = '0'*(n - len(tmp1[i])) + tmp1[i]
        tmp2[i] = '0'*(n - len(tmp2[i])) + tmp2[i]
                       
        tmp = ''
        for p in range(n):
            if tmp1[i][p] == '1' or tmp2[i][p] == '1':
                tmp += '#'
            elif tmp1[i][p] == '0' and tmp2[i][p] == '0':
                tmp += ' '
                
        answer.append(tmp)
        
    return answer