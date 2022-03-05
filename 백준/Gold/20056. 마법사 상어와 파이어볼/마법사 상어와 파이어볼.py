# 20056 마법사 상어와 파이어볼 
from sys import stdin
n, m, t = map(int, stdin.readline().split())
fire = []
for _ in range(m):
    fire.append(list(map(int, stdin.readline().split())))
    # 행+1 열+1 질량 방향 속력 
for i in range(len(fire)):
    fire[i][0], fire[i][1] = fire[i][0]-1, fire[i][1] -1
# 모든 파이어 볼이 자신의 방향 d로 속력 s칸만큼 이동한다. 
# 격자의 끝과 끝은 연결 
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
for _ in range(t):
    visit = [[[0, 0, 0, 10] for _ in range(n)] for _ in range(n)]
    for i in range(len(fire)):
        r, c, m, s, d = fire[i]
        a, b = (r + s*dx[d])%n , (c + s*dy[d])%n
        visit[a][b][0] += 1 # 갯수
        visit[a][b][1] += m # 질량
        visit[a][b][2] += s # 속도
        if visit[a][b][3] == 10: # 방향
               visit[a][b][3] = d # 첫방문일 경우 d로 초기화
                
        elif visit[a][b][3]%2 == d%2: # 아니면 0, 2, 4, 6
               pass
        else:
            visit[a][b][3] = -1 # -1이면 1, 3, 5
    
    fire = []
    for a in range(n):
        for b in range(n):
            if visit[a][b][0] >= 2:
                newm, news = visit[a][b][1]//5, visit[a][b][2]//visit[a][b][0]
                newd = False if visit[a][b][3] == -1 else True
                if newm > 0:
                    if newd == True: # 0, 2, 4, 6
                        for k in [0, 2, 4, 6]:
                            fire.append([a, b, newm, news, k])

                    else: # 1, 3, 5, 7
                        for k in [1, 3, 5, 7]:
                            fire.append([a, b, newm, news, k])
                else:
                    visit[a][b] = [0, 0, 0, 10]
        
        
            if visit[a][b][0] == 1:
                fire.append([a, b, visit[a][b][1], visit[a][b][2], visit[a][b][3]])
                
ans = 0
for k in fire:
    ans += k[2]
print(ans)