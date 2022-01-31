from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def choose(k):
    global i, n, visit
    if(not temp[k][1] in visit): # 방문 리스트에 안 나왔던 숫자임
        visit.append(temp[k][1])
        choose(temp[k][1]) # 해당 인덱스를 방문
    if(k == i and i in visit):
        return visit
    else:
        return None
    
n = int(stdin.readline())
num, temp = [], [[0,0]]
for i in range(n):
    num.append(int(stdin.readline().rstrip()))
for a, b in enumerate(num):
    temp.append([a+1,b])
del num

ans = set()
for i in range(0, n+1):
    visit, flag = [], 0 
    visited = choose(i)
    if(visited != None):
        for v in visited:
            ans.add(v)
if(len(ans) == 0):
    print(0)
else:
    print(len(ans) - 1)
ans = list(ans)
ans.sort()
for i in range(len(ans)):
    if(i !=0):
        print(ans[i])