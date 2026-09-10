def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(max(citations)):
        max_count = 0
        for j in citations:
            if j >= i:
                max_count += 1
        
        if len(citations) - max_count <= i and max_count >= i:
            answer = i
            
    
    return answer