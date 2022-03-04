# 20055 컨베이어 벨트 위의 로봇
from sys import stdin
n, k = map(int, stdin.readline().split())
belt = list(map(int, stdin.readline().split()))
rb = [0 for _ in range(n)]
m = 1
while(1):
    belt = [belt[-1]] + belt[0: 2*n-1]
    rb = [0] + rb[0:n-1]

    if rb[n-1]: rb[n-1] = 0

    for i in range(n-1, -1, -1):
        if rb[i] and belt[i+1] >= 1 and not rb[i+1]:
            rb[i+1], rb[i] = rb[i], 0
            belt[i+1] -= 1

    if rb[n-1]: rb[n-1] = 0

    if belt[0] > 0:
        rb[0] = 1
        belt[0] -= 1

    cnt = 0
    for i in range(2*n):
        if belt[i] == 0:
            cnt += 1
    if cnt >= k:
        print(m)
        break
    m += 1
