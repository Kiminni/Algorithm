def solution(a, b, c, d):
    answer = 0
    check = len(set([a,b,c,d]))
    set_ans = set([a,b,c,d])
    if check == 1:
        return 1111 * a
    
    elif check == 4:
        return min(set([a,b,c,d]))
    
    elif check == 2:
        if a == b == c :
            return (10 * a + d)**2
        
    
        elif a == b == d :
            return (10 * a + c)**2
        
        elif a == c == d :
            return (10 * a + b)**2
        
        elif d == b == c :
            return (10 * b + a)**2
        
        elif a == b and c == d:
            return (a + c) * abs(a - c)
        
        elif a == c and b == d:
            return (a + b) * abs(a - b)
        
        elif a == d and b == c:
            return (a + b) * abs(a - b)
    
    if check == 3:
        if a == b:
            return c * d
        elif a == c:
            return b * d
        elif a == d:
            return b * c
        elif b == c :
            return a * d
        elif b == d:
            return a * c
        elif c == d:
            return a * b
        
        