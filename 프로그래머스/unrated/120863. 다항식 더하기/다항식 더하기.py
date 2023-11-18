def solution(polynomial):
    answer = ''
    poly_list = polynomial.split(' ')
    x_list = []
    num_list = []
    sep_list = []
    
    for pol in poly_list:
        if pol == 'x':
            pol = '1'
            x_list.append(int(pol))
            
        elif 'x' in pol:
            pol = pol[0:len(pol)-1]
            x_list.append(int(pol))
            
        elif '0' <= pol <= '99':
            num_list.append(int(pol))
            
        elif pol == '+':
            sep_list.append(pol)

    
    if x_list == [] and num_list == [] : # Empty
        return polynomial
    
    if sum(x_list) == 0: # 계수가 0 (정수만)
        return str(sum(num_list))
    
    elif sum(x_list) > 1: # 계수 1 이상
        answer = str(sum(x_list)) + 'x'
        
    elif sum(x_list) == 1:  # 계수 1
        answer = 'x'
    
    else:
        answer = ' '

    if sum(num_list) >= 1: # 상수 1 이상
        return answer + " + " + str(sum(num_list))
        
    return answer 