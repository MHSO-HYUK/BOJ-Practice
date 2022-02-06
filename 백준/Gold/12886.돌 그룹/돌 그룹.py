#12886 돌 그룹
# 모든 그룹의 돌 개수를 같게
# 크기가 다른 두 그룹을 고른다. 
# X = X+X / Y = Y-X 개로 만든다.
import sys
from sys import stdin
from collections import defaultdict
sys.setrecursionlimit(10**6)
def rock(x, y, z):
    visit[tuple([x,y,z])] = True
    if(x == y == z):
        print(1)
        sys.exit()
    if(x < y):
        x, y = x+x, y-x
        if(not visit[tuple([x,y,z])]):
            visit[tuple([x,y,z])] = True
            rock(x, y, z)
    if(x > y):
        x, y = x-y, y+y
        if(not visit[tuple([x,y,z])]):
            visit[tuple([x,y,z])] = True
            rock(x, y, z)
    if(y < z):
        y, z = y+y, z-y
        if(not visit[tuple([x,y,z])]):
            visit[tuple([x,y,z])] = True
            rock(x, y, z)
    if(y > z):
        y, z = y-z, z+z
        if(not visit[tuple([x,y,z])]):
            visit[tuple([x,y,z])] = True
            rock(x, y, z)
    if(z < x):
        z, x = z+z, x-z
        if(not visit[tuple([x,y,z])]):
            visit[tuple([x,y,z])] = True
            rock(x, y, z)
    if(z > x):
        z, x = z-x, x+x
        if(not visit[tuple([x,y,z])]):
            visit[tuple([x,y,z])] = True
            rock(x, y, z)

a, b, c = map(int, stdin.readline().split())
visit = defaultdict(bool)
if (a+b+c)%3:
    print(0)
else:
    temp = rock(a,b,c)
    if(temp == None):
        print(0)