from collections import deque
def solution(priorities, location):
    answer = []
    queue = deque(priorities)
    idx = deque([_ for _ in range(len(priorities))])
    while queue:
        process = queue.popleft()
        if len(queue) > 0 and max(queue) > process:
            queue.append(process)
            idx.append(idx.popleft())
        else:
            answer.append(idx.popleft())
            
    return answer.index(location) + 1