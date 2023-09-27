def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in skip:
        alphabet = alphabet.replace(i, "")
    for i in s:
        change = alphabet[(alphabet.index(i)+index)% len(alphabet)]
        answer += change
    return answer