#2579 계단오르기
# 3연속 계단을 밟을 순 없음
from collections import deque
from sys import stdin
def stair():
    queue = deque()
    queue.append([0, 0, 0])    
    while(queue):
        now, con, score = queue.popleft()
        for k in [1, 2]:
            next = now+k
            if next <= n:
                if k == 1 and con + 1 !=  3 and visit[next][con+1] <= score+st[next]:
                    visit[next][con+1] = score+st[next]
                    queue.append([next, con+1, score+st[next]])

                if k == 2 and visit[next][1] <= score+st[next]:
                    visit[next][1] = score+st[next]
                    queue.append([next, 1, score+st[next]])

    return max(visit[-1])
       
n = int(stdin.readline())
dp = [0 for _ in range(n+1)]
st = [0]
for _ in range(n):
    st.append(int(stdin.readline()))
visit = [[0,0,0] for _ in range(n+1)]
print(stair())