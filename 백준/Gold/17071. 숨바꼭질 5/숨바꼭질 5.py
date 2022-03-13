# 17071 숨바꼭질 5
from sys import stdin 
import sys
from collections import deque
from collections import defaultdict

n, k= map(int, stdin.readline().split())
# 1초 뒤 +1, -1 
# 1초 뒤 2*n
# 동생은 매초 이동을 하며 가속이 붙음 
queue = deque([[n, 0]])
odd = defaultdict(int)
even = defaultdict(int)
odd[n] = 1
while(queue):
    for _ in range(len(queue)):
        now, sec = queue.popleft()
        if now == k:
            print(sec)
            sys.exit()
            
        if sec%2:
            if 2*now <= 500000 and not odd[2*now]:
                odd[2*now] = 1
                queue.append([2*now, sec+1])
                
            if now+1<= 500000 and not odd[now+1]:
                odd[now+1] = 1
                queue.append([now+1, sec+1])
                
            if now-1 >=0 and not odd[now-1] :
                odd[now-1] = 1
                queue.append([now-1, sec+1])

        else:   
            if 2*now <= 500000 and not even[2*now]:
                even[2*now] = 1
                queue.append([2*now, sec+1])
                
            if now+1<= 500000 and not even[now+1]:
                even[now+1] =1 
                queue.append([now+1, sec+1])
                
            if now-1 >=0 and not even[now-1]:
                even[now-1] = 1
                queue.append([now-1, sec+1])

    
    k += sec+1
    if k > 500000:
        print(-1)
        break
    else:
        if sec%2 and k in odd:
            print(sec+1)
            break
        if not sec%2 and k in even:
            print(sec+1)
            break