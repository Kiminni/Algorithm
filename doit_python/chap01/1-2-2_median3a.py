def med3(a,b,c):

    if(b >= a and c<= a) or (c >= a and b <= a):
        return a
    
    elif(a > b and b < c) or (c < b and b < a):
        return b
    
    return c

# 비효율