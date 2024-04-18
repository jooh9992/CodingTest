from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        course_dict = {}  # course에 해당하는 메뉴 조합의 등장 횟수를 저장할 딕셔너리 생성
        for o in orders:
            for comb in combinations(sorted(o), c):  # 메뉴 조합 생성
                comb_str = ''.join(comb)
                if comb_str in course_dict:
                    course_dict[comb_str] += 1
                else:
                    course_dict[comb_str] = 1
        
        # course_dict에서 가장 많이 등장한 메뉴 조합 찾기
        max_count = 0
        max_combinations = []
        for key, value in course_dict.items():
            if value > max_count:
                max_count = value
                max_combinations = [key]
            elif value == max_count:
                max_combinations.append(key)
        
        # 최빈값이 2 이상이면 answer에 추가
        if max_count >= 2:
            answer += max_combinations

    return sorted(answer)