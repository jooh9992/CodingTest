#시간 계산 함수
def times(start_t, end_t):
    h1, m1 = start_t.split(":")
    h2, m2 = end_t.split(":")
    
    start_time = int(h1)*60 + int(m1)
    end_time = int(h2)*60 + int(m2)
    
    return end_time - start_time

#치환
def tranceCode(code):
    code = code.replace("C#", "c")
    code = code.replace("D#", "d")
    code = code.replace("F#", "f")
    code = code.replace("G#", "g")
    code = code.replace("A#", "a")
    code = code.replace("B#", 'b')
    return code
    
def solution(m, musicinfos):
    answer = []
    m = tranceCode(m)
    
    for i, music in enumerate(musicinfos):
        mu = music.split(",")
        time = times(mu[0], mu[1])
        title = mu[2]
        code = tranceCode(mu[3])
        
        while len(code) < time:
            code += code
        code = code[:time]
        
        if m in code:
            answer.append([time, i, title])
            
    if answer:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]
    else:
        return "(None)"