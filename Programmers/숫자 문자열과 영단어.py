def solution(s):
    answer = 0
    dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
             'seven': 7, 'eight': 8, 'nine': 9}

    for x, y in dict1.items():
        s = s.replace(x, str(y))

    return int(s)