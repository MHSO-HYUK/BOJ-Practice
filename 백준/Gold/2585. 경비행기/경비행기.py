from collections import deque
import sys, math
input = sys.stdin.readline
n, k = map(int, input().split())
airport = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
def BFS(vertex, fuel):
    visit = [False] * (n + 1)
    landingCount = 0
    dq = deque()
    dq.append(vertex)
    while len(dq):
        if landingCount > k:
            return False
        for _ in range(len(dq)):
            vertex = dq.popleft()
            if not visit[vertex]:
                visit[vertex] = True
                for i in range(1, n + 1):
                    distance = math.sqrt(
                        pow(airport[vertex][0] - airport[i][0], 2) + pow(airport[vertex][1] - airport[i][1], 2))

                    if distance <= fuel:
                        distanceForDestination = math.sqrt(
                            pow(10000 - airport[i][0], 2) + pow(10000 - airport[i][1], 2))

                        if distanceForDestination <= fuel:
                            return True

                        dq.append(i)

        landingCount += 1
    return False

left = 0
right = 100000
result = 0

while left <= right:
    mid = (left + right) // 2

    if BFS(0, mid * 10):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)