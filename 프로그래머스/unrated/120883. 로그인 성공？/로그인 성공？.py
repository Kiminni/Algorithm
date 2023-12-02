def solution(id_pw, db):
    answer = ''
    for query in db:
        if id_pw[0] == query[0]:
            if id_pw[1] == query[1]:
                return "login"
            
            return "wrong pw"
        
    return "fail"