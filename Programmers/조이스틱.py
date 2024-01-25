def solution(name):
    
    s_move = 0

    c_move = len(name) - 1  
    
    
    for i, spell in enumerate(name):
        s_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        c_move = min([ c_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])
        
    return s_move + c_move