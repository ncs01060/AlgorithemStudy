from collections import deque
def solution(maps):
    answer = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    visited = [[False] * len(_) for _ in maps]


    for i in range(0,len(maps)):
        
        for j in range(0,len(maps[i])):
            if maps[i][j] != 'X' and not visited[i][j]:
                count = 0
                queue = deque([[i,j]])
                visited[i][j] = True
                count += int(maps[i][j])
                
                while queue:
                    x,y = queue.popleft() # type: ignore
                    for k in range(4):
                        nx,ny = x + dx[k] , y + dy[k]
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] != True and maps[nx][ny] != 'X':
                            count += int(maps[nx][ny])    
                            queue.append([nx,ny]) # type: ignore
                            visited[nx][ny] = True
                answer.append(count)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer