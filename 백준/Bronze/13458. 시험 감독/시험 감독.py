# 13458 시험 감독
# 한 방에 총감독은 1명만 + 부감독은 여러명
from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b, c = map(int, stdin.readline().split())
total = len(a)
for human in a:
    temp = human - b
    if temp > 0:
        total += temp // c
        if temp % c:
            total += 1
print(total)