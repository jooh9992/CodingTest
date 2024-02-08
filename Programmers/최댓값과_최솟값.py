def solution(s):
    int_list = list(map(int, s.split(" ")))
    return str(min(int_list)) + " " + str(max(int_list))