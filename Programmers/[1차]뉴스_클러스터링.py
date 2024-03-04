def solution(str1, str2):
    str1_li, str2_li = [], []
    int_li= []
    
    #대문자 만들기
    str1 = str1.upper()
    str2 = str2.upper()
    
    #두 글자씩 끊어서 다중 집합 만들기
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_li.append(str1[i:i+2])
            
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_li.append(str2[i:i+2])
        
    #교집합
    tmp = str2_li.copy()
    for i in str1_li:
        if i in tmp:
            int_li.append(i)
            tmp.remove(i)

    #합집합 개수
    uni = len(str1_li) + len(str2_li) - len(int_li)
    
    #출력
    if len(str1_li) == len(str2_li) == 0:
        return 65536
    else:
        return int((len(int_li) / uni) * 65536)