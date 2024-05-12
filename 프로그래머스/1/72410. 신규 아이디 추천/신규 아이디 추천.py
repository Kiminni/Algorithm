"""
1. 소문자 치환
2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 제외 다 삭제
"""
def solution(new_id):
    answer = ''
    check = ["-", "_", "."]
    tmp = []
    new_id = new_id.lower()
    for new in new_id:
        if new.isalpha() or new.isdigit() or new in check:
            tmp.append(new)
    new_id = ''.join(tmp)
    while ".." in new_id:
        new_id = new_id.replace("..",".")
    
    if len(new_id) > 0:
        if new_id[0] == "."  :
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    if new_id == "":
        new_id += "a"
    
    if len(new_id) > 15:
        new_id = new_id[:15]
        for i in range(len(new_id)):
            if new_id[-1] == ".":
                new_id = new_id[:-1]
                
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id