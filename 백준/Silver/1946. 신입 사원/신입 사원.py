#1946
from sys import stdin
t = int(stdin.readline())
ans = []
for i in range(t):
    cnt = 1
    people = []
    n = int(stdin.readline())
    for i in range(n):
        a, b = map(int,stdin.readline().split())
        people.append([a,b])
    people.sort()
    maxima = people[0][1]
    
    for i in range(1, n):
        if maxima > people[i][1]:
            cnt += 1
            maxima = people[i][1]
    ans.append(cnt)
    
for i in range(t):
    print(ans[i])