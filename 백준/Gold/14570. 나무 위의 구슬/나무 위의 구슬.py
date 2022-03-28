# 14570 나무 위의 구슬
from sys import stdin
n = int(stdin.readline())
graph = [[-1, -1] for _ in range(n+1)]
bizz = [[0 ,0] for _ in range(n+1)]
for i in range(1, n+1):
    u, v = map(int, stdin.readline().split())
    if u != -1:
        graph[i][0] = u
    if v != -1:
        graph[i][1] = v
k = int(stdin.readline())
now = 1
while(k >= 0):
    dirc = k % 2
    left, right = graph[now][0], graph[now][1]
    if left != - 1 and right != -1:
        if dirc:
            now = left
        else:
            now = right
        k = k // 2 + dirc
    else:
        if left == -1 and right == -1:
            break
        elif right == -1:
            now = left
        else:
            now = right
print(now)