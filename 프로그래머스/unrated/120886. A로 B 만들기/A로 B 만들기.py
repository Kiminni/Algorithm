def solution(before, after):
    
    set_before = list(before)
    set_after = list(after)
    if sorted(set_after) == sorted(set_before):
        return 1
    return 0