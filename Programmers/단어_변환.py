from collections import deque

def match(word1, word2):
    # word1 과 word2가 한글자 차이가 나는지 확인하는 함수
    count = sum(a != b for a, b in zip(word1, word2))
    return count == 1

def solution(begin, target, words):

    if target not in words: #변환 할 수 없는 경우
        return 0
    
    visited = set() #방문한 단어를 기록하기 위한 집합
    queue = deque([(begin, 0)]) #BFS를 위한 큐 [(단어, 변환 횟수)]

    while queue:
        current_word, step = queue.popleft()

        if current_word == target:
            return step # 타겟 단어를 찾았을 때 현재까지의 변환 횟수 반환
        
        for word in words:
            if word not in visited and match(current_word, word):
                visited.add(word)
                queue.append([word, step+1])
    
    return 0

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])