def solution(n, lost, reserve):
    
    
    _lost = lost.copy()
    _reserve = reserve.copy()

    _lost.sort()
    _reserve.sort()
    
    for s in lost:
        if s in _reserve:
            _lost.remove(s)
            _reserve.remove(s)

    answer = n - len(_lost)
    for i in range(len(_lost)):
        if _lost[i] in _reserve:
            _reserve.remove(_lost[i])
            answer+=1
            continue
        elif _lost[i] - 1 in _reserve:
            answer+=1
            _reserve.pop(_reserve.index(_lost[i] - 1))
        elif _lost[i] + 1 in _reserve:
            answer += 1
            _reserve.pop(_reserve.index(_lost[i] + 1))
    return answer