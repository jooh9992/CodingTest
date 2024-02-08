def solution(my_string):
    answer = ''
    list = []
    for i in my_string:
        if i not in list:
            list.append(i)
            
    return "".join(list)