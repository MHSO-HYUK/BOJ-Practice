from copy import deepcopy
n = int(input())
q = [list(input().rstrip()) for _ in range(n)]
flag = q[0]
for i in range(1, n):
    temp = []
    for v in range(len(flag)):
        if q[i][v] == flag[v]:
            temp.append(q[i][v])
        else:
            temp.append('?')
    flag = deepcopy(temp)
print(''.join(flag))