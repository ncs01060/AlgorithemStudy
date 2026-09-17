from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        count = 0
        num = queue.popleft()
        for i in queue:
            if num <= i:
                count += 1
            else:
                count+=1
                break
        answer.append(count)
                
    return answer