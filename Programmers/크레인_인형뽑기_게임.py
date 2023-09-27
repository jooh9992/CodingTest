def solution(board, moves):
    arr = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                arr.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(arr) > 1:
                    if arr[-1] == arr[-2]:
                        arr.pop(-1)
                        arr.pop(-1)
                        answer += 2
                break
    return answer