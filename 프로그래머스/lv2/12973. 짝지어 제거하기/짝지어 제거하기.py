def solution(s):
    stack = []
    for now in s:
        if len(stack) and stack[-1] == now:
            stack.pop()
        else:
            stack.append(now)
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    

    return answer