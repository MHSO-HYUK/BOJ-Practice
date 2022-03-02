# 13458 시험감독
# 총감독 b명 관찰 // 부감독 c명 관찰
# 총감독은 방에 1명 // 부김독은  방에 여러명  
from sys import stdin 

n = int(stdin.readline()) #시험장의 갯수
a = list(map(int, stdin.readline().split())) # 각 시험장에 있는 응시자 수
b, c = map(int, stdin.readline().split())
ans = 0
for i in range(n):
    temp = 0
    a[i] -= b
    if a[i] <= 0: ans += 1
    else:
        temp = 1
        if a[i] % c: temp += a[i] //  c + 1
        else: temp += a[i] // c
        ans += temp

print(ans)