def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        su=[]
        for j in range(len(arr1[i])):
            su.append(arr1[i][j] + arr2[i][j])
        answer.append(su)
    return answer