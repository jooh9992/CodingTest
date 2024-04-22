def solution(storey):
    answer = 0
    
    while storey > 0:
        storey, move = divmod(storey, 10)

        if move < 5 or (move == 5 and storey%10 < 5):
            answer += move
        else:
            answer += (10 - move)
            storey += 1
    return answer