def solution(my_string, queries):
    answer = ''
    list_string = list(my_string)
    for query in queries:
        sub_string = list_string[query[0] : query[1] + 1]
        sub_string.reverse()
        idx = 0
        for i in range(query[0], query[1] + 1):
            list_string[i] = sub_string[idx]
            idx += 1
        
    return ''.join(list_string)