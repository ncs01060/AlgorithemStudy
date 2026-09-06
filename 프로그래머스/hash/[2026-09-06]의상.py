import math
def solution(clothes):
    answer = 0
    hash_map = {}
    for i in clothes:
        if i[1] not in hash_map:
            hash_map[i[1]] = 1
        hash_map[i[1]] += 1
            
    
    answer = math.prod(hash_map.values()) - 1
        
    return answer