import sys
def check(): # i번 세로선이 i번으로 도착하는지 확인
    for start in range(N): # 1번부터 N번 세로선(열)까지 검사
        k = start # k는 이동하는 가로선
        for j in range(H): # 가로선(행) 이동
            if board[j][k]: # 가로선이 존재한다면
                k += 1 # 가로선 오른쪽으로 한칸 이동
            elif k > 0 and board[j][k - 1]: # 가로선이 왼쪽에 존재한다면
                k -= 1 # 가로선 왼쪽으로 한칸 이동
        if k != start: return False # 가장 하단까지 왔는데 k가 start랑 같지 않으면 정상 도착하지 않은 것이므로 return False
    return True

def dfs(cnt, x, y):
    global ans
    if check(): # 현재 상태에서 각 출발점이 도착점으로 잘 도착하는지 확인
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt: # 도착점이 정상적이지 않으면
        return
    for i in range(x, H):
        # 가로선을 우선으로 탐색하므로
        if i == x: k = y # 행이 변경되기 전에는 가로선을 계속해서 탐색
        else: k = 0 # 행이 변경될 경우 가로선 처음부터 탐색
        for j in range(k, N - 1): # 세로선(열)
            if not board[i][j] and not board[i][j + 1]: # 가로선을 놨을 때 오른쪽에 -가 존재하지 않는 경우
                if j > 0 and board[i][j - 1]: continue # 가로선을 놨을 때 왼쪽에 -가 존재할 경우 continue (--가 되면 안되기 때문)
                board[i][j] = True # 가로선 놓기
                dfs(cnt + 1, i, j + 2) # cnt 1 증가, 세로선 그대로, -- 이 되면 안되므로 가로선은 2증가
                board[i][j] = False # 가로선 없애기

                
N, M, H = map(int, sys.stdin.readline().split())
board = [[False] * N for _ in range(H)] # 특정 지점 방문 여부 체크
if M == 0: # M이 0일 경우 출발점에서 도착점으로 바로 내려오므로 0 출력 후 종료
    print(0)
    exit(0)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = True
ans = 4 # 결과값 4로 초기화
dfs(0, 0, 0)
print(ans if ans < 4 else -1)