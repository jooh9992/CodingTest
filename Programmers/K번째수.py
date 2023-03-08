def solution(array, commands):
    answer = []

    for x, y, z in commands:
        arr = array[x-1:y]
        arr.sort()
        answer.append(arr[z-1])
    return answer