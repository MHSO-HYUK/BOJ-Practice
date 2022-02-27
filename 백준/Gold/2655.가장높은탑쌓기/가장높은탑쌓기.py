# 2655 가장 높은 탑 쌓기
# 회전 불가  // 밑면이 좁아지면서 올라간다 // 무게가 줄어들면서 올라간다.
from sys import stdin
n = int(stdin.readline())
inf = []
for idx in range(n):
    d, h, w = map(int, stdin.readline().split())
    inf.append([w, d, h, idx+1]) # 무게 / 밑면 / 높이 / 인덱스 순

inf.sort(key= lambda x : x[0]) # 무게 내림 차순으로 정렬 
dp =  [inf[i][2] for i in range(n)]
for i in range(n):
    for j in range(i):
        if inf[i][1] > inf[j][1]:
            dp[i] = max(dp[i], dp[j]+inf[i][2])

temp1 = dp.index(max(dp))
temp2 = temp1 - 1
ans = [inf[temp1][3]]
if temp1 == 0:
    print(1)
    print(ans[0])
else:
    while(1):
        if inf[temp1][1] > inf[temp2][1] and dp[temp2] == dp[temp1] - inf[temp1][2]:
            ans.append(inf[temp2][3])
            temp1, temp2 = temp2, temp2-1
            if temp2 < 0:
                break
        else:
            temp2 -= 1
            if temp2 < 0:
                break
    print(len(ans))
    for i in range(len(ans)):
        print(ans[len(ans)- 1- i])