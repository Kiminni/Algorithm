def solution(s):
    list_s = s.split(" ")
    list_j = []
    for i in list_s:
        for j in range(len(i)):
            if j == 0 and 'a' <= i[j] <= 'z':
                list_j.append(i[j].upper())
            elif j == 0 and "A" <= i[j] <= "Z":
                list_j.append(i[j])
            else:
                list_j.append(i[j].lower())
        list_j.append(" ")
    list_j.pop()
    return ''.join(list_j)
    

            