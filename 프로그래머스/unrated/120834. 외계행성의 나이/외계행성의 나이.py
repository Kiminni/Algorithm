def solution(age):
    
    alpha=['a','b','c','d','e','f','g','h','i','j']
    
    i = age
    tmp = ''
    while i > 0:
        tmp += alpha[i % 10]
        i = i // 10
        
    return tmp[::-1]