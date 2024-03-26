def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)
    
    while dp:
        if y in dp:
            return answer
        else:
            case = set()
            for i in dp:
                if i+n <= y:
                    case.add(i+n)
                if i*2 <= y:
                    case.add(i*2)
                if i*3 <= y:
                    case.add(i*3)
            dp = case
            answer += 1
            
    return -1