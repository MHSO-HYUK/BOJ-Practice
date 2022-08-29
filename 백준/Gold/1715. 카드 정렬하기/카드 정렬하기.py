from sys import stdin
import heapq
n = int(stdin.readline())
a = []
for i in range(n):
    a.append(int(stdin.readline()))
heapq.heapify(a)
ans = 0
while(len(a) != 1):
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    heapq.heappush(a, x+y)
    ans += x+y
print(ans)