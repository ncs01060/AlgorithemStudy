from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    queue = deque([0] * (bridge_length))
    weigh = 0

    while sum(queue) != 0 or truck_weights:
        weigh = weigh - queue.popleft()
        if truck_weights:
            if weigh + truck_weights[0] <= weight:
                num = truck_weights.popleft()
                queue.append(num)
                weigh += num
            else:
                queue.append(0)
        else:
            queue.append(0)

        answer+=1

    return answer