def solution(cacheSize, cities):
    answer = 0
    i = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if i < cacheSize:
                cache.append(city)
                i += 1
            else:
                cache.pop(0)
                cache.append(city)

    return answer