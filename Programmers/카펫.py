def solution(brown, yellow):
    #노란색 크기를 구해서 전체 크기를 구하도록 구현
    #약수를 사용
    for i in range(1,yellow+1):
        if(yellow % i ==0):
            yellow_row = (yellow /i)
            yellow_col = i
            if (2 * (yellow_row + yellow_col) + 4 == brown):
                return [yellow_row +2, yellow_col+2]