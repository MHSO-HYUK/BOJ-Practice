#9019 DSLR
# D: 2n % 10000
# S: n-1
# L: 왼쪽 시프트 
# R: 오른쪽 시프트
from sys import stdin
from collections import deque

def DSLR(s, f):
    queue = deque()
    queue.append([s, []])
    visit = [0 for _ in range(10**4)]
    visit[s] = 1
    while(queue):
        p, com = queue.popleft()
        a, b, c, d = p//1000, (p%1000)//100, (p%100)//10, p%10
        if(p == f):
            return com
        if(visit[(2*p) % 10000] == 0 and p != 0):
            visit[(2*p) % 10000] = 1
            queue.append([(2*p) % 10000, com+['D']])
            
        if(p == 0 and visit[9999] == 0):
            visit[9999] = 1
            queue.append([9999, com+['S']])
            
        if(p-1 >= 0 and visit[p-1] == 0):
            visit[p-1] = 1
            queue.append([p-1, com+['S']])
            
        if(visit[1000*b+100*c+10*d+a] == 0):
            visit[1000*b+100*c+10*d+a] = 1
            queue.append([1000*b+100*c+10*d+a, com+['L']])

        if(visit[1000*d + 100* a + 10*b + c] == 0):
            visit[1000*d + 100* a + 10*b + c] = 1
            queue.append([1000*d+100*a+10*b+c, com+['R']])

n = int(stdin.readline())
for _ in range(n):
    s, f = map(int, stdin.readline().split())
    ans = DSLR(s, f)
    for i in range(len(ans)):
        print(ans[i], end = '')
    print()