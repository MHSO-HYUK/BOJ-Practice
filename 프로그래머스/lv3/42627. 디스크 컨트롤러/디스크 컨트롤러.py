import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    time = jobs[0][0]
    i = 0
    heap = []
    trial = 0
    
    while(True):
        while(True):
            if i < len(jobs) and jobs[i][0]  <= time:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0], i]) # 수행 가능한 Task를 heap에 
                i += 1
            else:
                break
        
        if trial != len(jobs) and len(heap) == 0:
            time = jobs[i][0]
            continue
        
        if trial == len(jobs):
            return answer // len(jobs)
        
        now = heapq.heappop(heap) # 수행 시간 가장 짧은 Task 수행
        trial += 1
        answer += (time - now[1] + now[0])
        time += now[0]
        