import math
def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(0,len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    count = 1
    max_queue = queue.pop(0)
    
    while queue:
        if max_queue >= queue[0]:
            queue.pop(0)
            count += 1
        else:
            max_queue = queue.pop(0)
            answer.append(count)
            count = 1
        
    answer.append(count)
    return answer