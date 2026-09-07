
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] >= K:
        return answer
    
    while True:
        if len(scoville) == 1 and scoville[0] >= K:
            answer = 0
            break
        elif len(scoville) <= 1:
            answer = -1
            break
        small_1 = heapq.heappop(scoville) 
        small_2 = heapq.heappop(scoville)

        plus_scoville = small_1 + (small_2 * 2)

        heapq.heappush(scoville, plus_scoville)
        answer += 1
        
        if scoville[0] >= K:
            break
        
    return answer