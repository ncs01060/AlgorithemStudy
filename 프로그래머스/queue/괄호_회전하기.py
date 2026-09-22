from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)
    
    count = 0
    while count != len(s):
        
        count += 1
        queue.append(queue.popleft())
        stack = [queue[0]]
        
        for i in range(1,len(queue)):
            if queue[i] == '(' or queue[i] == '{' or queue[i] =='[':
                stack.append(queue[i])
            else:
                if len(stack) != 0:
                    if queue[i] == ')' and stack[-1] == '(':
                        stack.pop()
                    elif queue[i] == '}' and stack[-1] == '{':
                        stack.pop()
                    elif queue[i] == ']' and stack[-1] == '[':
                        stack.pop()
        if len(stack) == 0:
            answer += 1
    
    return answer

print(solution("[](){}"))