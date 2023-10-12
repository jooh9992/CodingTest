def solution(players, callings):
    dic = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = dic[call]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        dic[players[idx]] = idx
        dic[players[idx-1]] = idx-1
    
    return players