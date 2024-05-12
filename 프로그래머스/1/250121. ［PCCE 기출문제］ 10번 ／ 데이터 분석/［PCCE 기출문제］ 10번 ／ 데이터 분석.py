def solution(data, ext, val_ext, sort_by):
    answer = []
    for d in data:
        if ext == "code":
            if d[0] < val_ext:
                answer.append(d)
        elif ext == "date":
            if d[1] < val_ext:
                answer.append(d)
        elif ext == "maximum":
            if d[2] < val_ext:
                answer.append(d)
        else:
            if d[3] < val_ext:
                answer.append(d)

    for i in range(len(answer)):
        if sort_by == "code":
            answer = sorted(answer, key=lambda answer:answer[0])
        elif sort_by == "date":
            answer = sorted(answer, key=lambda answer:answer[1])
        elif sort_by == "maximum":
            answer = sorted(answer, key=lambda answer:answer[2])
        else:
            answer = sorted(answer, key=lambda answer:answer[3])
    
    return answer