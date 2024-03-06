def solution(msg):
    answer = []
    words = {chr(idx+64):idx for idx in range(1, 27)} #색인 번호 딕셔너리 생성
    cnt = 27

    while True:
        i = 0
        if msg in words:
            answer.append(words[msg])
            return answer
        else:
            for j in range(1, len(msg)+1):
                if msg[i:j] not in words:
                    answer.append(words[msg[i:j-1]])
                    words[msg[i:j]] == cnt
                    cnt += 1

                    msg = msg[j-1:]
                    break