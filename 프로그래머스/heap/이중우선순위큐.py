import heapq
def solution(operations):
    answer = []
    heap = []
    heapq.heapify(heap)
    for i in operations:
        cmd, num = i.split()
        if cmd == "I":
            heapq.heappush(heap,int(num))
        elif cmd == "D" and int(num) == 1:
            if len(heap) != 0:
                heap.remove(max(heap))
        elif cmd == "D" and int(num) == -1:
            if len(heap) != 0:
                heapq.heappop(heap)
            
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer = [0,0]
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))