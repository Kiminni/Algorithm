T = int(input())
for k in range(T):
    iter, string = map(str, input().split())
    list_string = list(string)
    tmp = []    
    for i in range(len(list_string)): # 문자열 자체를 도는거고
        for j in range(int(iter)): # 반복 횟수 
            tmp.append(list_string[i]) # A A A B B B C C C
    print("".join(tmp))
