from collections import deque


def solution(maps):
    answer = 0
    queue = deque([[0,0]])
    visited = []


    dx = [1 ,0 ,-1 ,0]
    dy = [0, 1, 0 ,-1]

    while queue:

        x,y = queue.popleft()

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            answer = maps[x][y]
            break

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                visited.append([nx,ny])
                queue.append([nx,ny])
                maps[nx][ny] = maps[x][y] + 1

    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))