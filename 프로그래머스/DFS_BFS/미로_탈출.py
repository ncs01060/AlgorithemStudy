from collections import deque
def solution(maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = [i, j,0]
            elif maps[i][j] == 'L':
                lever = [i, j,0]
    
    
    answer = 0
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[start[0]][start[1]] = True # type: ignore
    queue = deque([start]) # type: ignore
    result = -1
    while queue:
        x,y,dist = queue.popleft() # type: ignore
        
        if maps[x][y] == "L":
            result = dist
            break
        
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append([nx,ny,dist+1])
                visited[nx][ny] = True

    if result == -1:
        return -1
    dist1 = result

    
    queue = deque([lever]) # type: ignore
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[lever[0]][lever[1]] = True # type: ignore
    result = -1
    while queue:
        x,y,dist = queue.popleft() # type: ignore
        
        if maps[x][y] == "E":
            result = dist
            break
        
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append([nx,ny,dist+1])
                visited[nx][ny] = True
    if result == -1:
        return -1
    dist2 = result            
    return dist1 + dist2