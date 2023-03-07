def solution(n, arr1, arr2):
    answer = []
    arr = []
    for i in range(n):
        arr.append(bin(arr1[i] | arr2[i])[2:].zfill(n))

    for i in arr:
        answer.append(i.replace("0", " ").replace("1", "#"))

    return answer