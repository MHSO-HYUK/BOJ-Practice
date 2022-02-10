#9466 텀 프로젝트
# 사이클이 생기면 같은 팀
from sys import stdin
import sys 
sys.setrecursionlimit(10**5)
def make(i):
    global res
    visit[i] = 1
    cy.append(i)
    if(visit[like[i]] == 1): #만약 이미 사이클이 형성된 사람이면?
        if like[i] in cy:
            res += cy[cy.index(like[i]):]
        return
    else:
        make(like[i])
        

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    like =list(map(int, stdin.readline().split()))
    like.insert(0,0)
    visit = [0 for _ in range(n+1)]
    res = []
    for i in range(1, n+1):
        if(visit[i] == 0):
            cy = []
            make(i)   
    print(n - len(res))