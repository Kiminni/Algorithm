def solution(numbers, hand):
    answer = ''
    left = [1,4,7,'*']
    right = [3,6,9,'#']
    center = [2,5,8,0]
    tmp_left = '*'
    tmp_right = '#'
    
    for number in numbers:
        if number in left:
            answer += 'L'
            tmp_left = number
        
        elif number in right:
            answer += 'R'
            tmp_right = number
        
        else: # 2,5,8,0
            center_idx = center.index(number)
            
            if tmp_left in left:
                left_idx = left.index(tmp_left)
                left_dis = abs(center_idx - left_idx)
            
            else:
                left_idx = center.index(tmp_left)
                left_dis = abs(center_idx - left_idx) - 1
                
            if tmp_right in right:
                right_idx = right.index(tmp_right)
                right_dis = abs(center_idx - right_idx)
            
            else:
                right_idx = center.index(tmp_right)
                right_dis = abs(center_idx - right_idx) - 1
            
            if right_dis > left_dis:
                answer += 'L'
                tmp_left = number
            
            elif left_dis > right_dis:
                answer += 'R'
                tmp_right = number
                
            else:
                if hand == 'left':
                    answer += 'L'
                    tmp_left = number
                elif hand == 'right':
                    answer += 'R'
                    tmp_right = number
            
    return answer
                