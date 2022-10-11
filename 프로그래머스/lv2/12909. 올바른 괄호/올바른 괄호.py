def solution(s):
    stack = []
    for now in s:
        if now == ')':
            if len(stack) != 0 and stack[-1] == '(': stack.pop()
            else: stack.append(now)
        else:
            stack.append(now)
    
    answer = True if len(stack) == 0 else False
    return answer