from collections import deque
def solution(board):
    answer = 0
    # 직선도로 -> 100 / 코너 -> 500
    # 최소한의 비용으로 경주로를 건설할 수 있을까
    dx, dy =[1, -1, 0, 0], [0, 0, 1, -1] # 하, 상, 우, 좌    
    
    n = len(board)
    minima = 1e9
    visit = [[[1e9, 1e9, 1e9, 1e9] for _ in range(n)] for _ in range(n)]
    visit[0][0] = [0, 0, 0, 0]
    
    q = deque()
    if board[0][1] == 0:
        visit[0][1][2] = 100
        q.append([0, 1, 100, 2]) # x, y, 비용, 직전방향
    if board[1][0] == 0:
        visit[1][0][0] = 100
        q.append([1, 0, 100, 0])
    
    while(q):
        x, y, cost, dirc = q.popleft()
        if cost >= minima: continue
        if x == n-1 and y == n-1:
            if cost < minima:
                minima = cost
            continue
            
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if board[nx][ny] == 0:
                    if dirc == 0 or dirc == 1:
                        if k == 0 or k == 1:
                            if visit[nx][ny][k] > cost + 100:
                                visit[nx][ny][k] = cost + 100
                                q.append([nx, ny, cost + 100, k])
                        else:
                            if visit[nx][ny][k] > cost + 600:
                                visit[nx][ny][k] = cost + 600
                                q.append([nx, ny, cost + 600, k])

                    elif dirc == 2 or dirc == 3:
                        if k == 0 or k == 1:
                            if visit[nx][ny][k] > cost + 600:
                                visit[nx][ny][k] = cost + 600
                                q.append([nx, ny, cost + 600, k])
                        else:
                            if visit[nx][ny][k] > cost + 100:
                                visit[nx][ny][k] = cost + 100
                                q.append([nx, ny, cost + 100, k])
    
    return minima