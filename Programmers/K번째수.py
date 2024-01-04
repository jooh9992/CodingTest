def solution(array, commands):
    answer = []

    for x, y, z in commands:
        arr = array[x-1:y]
        arr.sort()
        answer.append(arr[z-1])
    return answer

#24.01.05
def solution(array, commands):
    answer = []
    
    for i in commands:
        list = sorted(array[i[0]-1:i[1]])
        answer.append(list[i[2-1]])
        
    return answer