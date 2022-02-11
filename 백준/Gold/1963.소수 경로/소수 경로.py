#1963 소수경로
# 네자리수 소수만 주어진다 -> 항상 네자리수를 유지하면서 변화해야함
from sys import stdin
import math
from collections import deque
def prime(k):
    for i in range(2, int(math.sqrt(k))+1):
        if(k % i == 0):
            return False
    return True

def sosu(a, b):
    visit = [0 for _ in range(10000)]
    visit[a] = 1
    queue = deque([[a, 0]])
    while(queue):
        now, cnt = queue.popleft()
        if(now == b):
            return cnt
        q,w,e,r = now//1000, (now//100) % 10, (now//10)%10, now%10
        for i in range(1, 10):
            if(not visit[i*1000 + w*100 + e* 10 + r] and prime(i*1000 + w*100 + e* 10 + r)):
                visit[i*1000 + w*100 + e* 10 + r] = 1
                queue.append([i*1000 + w*100 + e* 10 + r, cnt + 1])
        for i in range(10):
            if(not visit[q*1000 + i*100 + e* 10 + r] and prime(q*1000 + i*100 + e* 10 + r)):
                visit[q*1000 + i*100 + e* 10 + r] = 1
                queue.append([q*1000 + i*100 + e* 10 + r, cnt + 1])
        for i in range(10):
            if(not visit[q*1000 + w*100 + i* 10 + r] and prime(q*1000 + w*100 + i* 10 + r)):
                visit[q*1000 + w*100 + i* 10 + r] = 1
                queue.append([q*1000 + w*100 + i* 10 + r, cnt + 1])
        for i in range(10):
            if(not visit[q*1000 + w*100 + e* 10 + i] and prime(q*1000 + w*100 + e* 10 + i)):
                visit[q*1000 + w*100 + e* 10 + i] = 1
                queue.append([q*1000 + w*100 + e* 10 + i, cnt + 1])


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    print(sosu(n, m))
