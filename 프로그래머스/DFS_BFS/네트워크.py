from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(len(computers)):

        if not visited[i]:
            queue = deque([i])
            visited[i] = True

            while queue:
                num = queue.popleft()
                for j in range(n):
                    if computers[num][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            answer+=1



        
    return answer

print(solution(	3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]))