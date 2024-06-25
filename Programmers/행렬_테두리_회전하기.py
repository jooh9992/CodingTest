def solution(rows, columns, queries):
    answer = []
    
    matrix = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            matrix[row][col] = t
            t += 1
    
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1-1][y1-1]
        small = tmp
        
        #왼쪽
        for i in range(x1-1, x2-1):
            a = matrix[i+1][y1-1]
            matrix[i][y1-1] = a
            small = min(a, small)
            
        #아래
        for i in range(y1-1, y2-1):
            a = matrix[x2-1][i+1]
            matrix[x2-1][i] = a
            small = min(a, small)
            
        #오른쪽
        for i in range(x2-1,x1-1,-1):
            a = matrix[i-1][y2-1]
            matrix[i][y2-1] = a
            small = min(a, small)
        
        #위
        for i in range(y2-1,y1-1,-1):
            a = matrix[x1-1][i-1]
            matrix[x1-1][i] = a
            small = min(a, small)
        
        matrix[x1-1][y1] = tmp
        answer.append(small)
    
    
    return answer