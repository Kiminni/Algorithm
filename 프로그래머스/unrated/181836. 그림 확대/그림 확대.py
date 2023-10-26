def solution(picture, k):
    tmp_pic = []
    for pic in picture:
        tmp = ''
        for i in range(len(pic)):
            tmp += pic[i] * k
        for i in range(k):
            tmp_pic.append(tmp)
    return tmp_pic