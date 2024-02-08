def solution(sides):
    sides.sort()
    if sides[-1] < sum(sides[:-1]):
        return 1
    else:
        return 2