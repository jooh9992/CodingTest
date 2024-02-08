def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수
        # 첫번째 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 소문자로 만듦
        # 첫 문자가 알파벳이 아니면 그대로 리턴
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer