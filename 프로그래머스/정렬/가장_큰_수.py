def solution(numbers):
    max_num = 0
    
    for i in numbers:
        t = []
        answer = ""
        for j in i:
            t.append(int(j))
        t.sort()
        for k in t:
            answer += str(k)
        if max_num < int(answer):
            max_num = int(answer)
            
    return max_num

print(solution([6, 10, 2]))