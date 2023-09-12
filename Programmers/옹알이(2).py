def solution(babbling):
    count = 0
    babble = [ "aya", "ye", "woo", "ma" ]
    
    for word in babbling:
        for text in babble:
            if text * 2 not in word:
                word = word.replace(text, ' ')
        if word.strip() == '':
            count += 1
    return count