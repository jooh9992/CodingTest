def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    
    p = set()
    
    while True:
        # 붙어있는 블록의 좌표값을 set에 저장
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == [] :
                    continue
                elif board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    p.add((i, j))
                    p.add((i, j+1))
                    p.add((i+1, j))
                    p.add((i+1, j+1))
        
        # 좌표값이 있으면 블록 삭제
        if p :
            answer += len(p)
            for i,j in p :
                board[i][j] = []
            p = set()
        else :
            break
        
        # 삭제된 블록을 아래로 내리기
        while True :
            moved = 0
            for i in range(m-1) :
                for j in range(n) :
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
        
    return answer