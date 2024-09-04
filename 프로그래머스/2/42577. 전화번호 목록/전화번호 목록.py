def solution(phone_book):
    # 딕셔너리에 전화번호를 저장합니다.
    table = {}
    
    # 전화번호를 딕셔너리에 저장합니다.
    for phone in phone_book:
        table[phone] = True
    
    # 모든 전화번호를 순회합니다.
    for phone in phone_book:
        # 접두어를 확인하기 위해 각 전화번호의 부분 문자열을 순회합니다.
        for i in range(1, len(phone)):
            # 접두어가 딕셔너리에 있는지 확인합니다.
            if phone[:i] in table:
                return False  # 접두어가 발견되면 False를 반환합니다.
    
    # 접두어가 없으면 True를 반환합니다.
    return True