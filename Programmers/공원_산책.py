def solution(park, routes):
    x, y = 0, 0
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x = i
                y = j

    for i in routes:
        a, b = i.split(" ")
        dx, dy = x, y  # 현재위치
        
        for i in range(int(b)):
            # 이동할 위치
            nx = x + op[a][0]
            ny = y + op[a][1]
        
            if 0<=nx<=len(park)-1 and 0<=ny<=len(park[0])-1 and (park[nx][ny]!="X"):
                x, y = nx, ny
                    
            else:
                x, y = dx, dy
                break
            
    return [x,y]

solution(["OOO", "OSO", "OOO", "OOO"],["N 2", "S 2"])