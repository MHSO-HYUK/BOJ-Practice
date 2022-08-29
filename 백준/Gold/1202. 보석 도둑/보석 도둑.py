import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

jewelryList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]
jewelryList.sort()
bagList.sort()

result = 0
temp = []

for bagWeight in bagList:
    while jewelryList and bagWeight >= jewelryList[0][0]:
        heapq.heappush(temp, -jewelryList[0][1])  # Max heap
        heapq.heappop(jewelryList)

    if temp:
        result += heapq.heappop(temp)
    elif not jewelryList:
        break

print(-result)