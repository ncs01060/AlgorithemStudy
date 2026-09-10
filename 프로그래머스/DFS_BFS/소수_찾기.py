def check(numbers,current,visited,prime:set):
    for i in range(0,len(numbers)):
        if visited[i]:
            continue
        else:
            visited[i] = True
            current+=numbers[i]
            if int(current) > 1:
                for j in range(2,int(current)):
                    if int(current) % j == 0:
                        break
                else:
                    prime.add(int(current))
            check(numbers,current,visited,prime)
            visited[i] = False
            current = current[:-1]
    return prime
    

def solution(numbers):
    prime = set()
    visited = [False] * len(numbers)
    answer = check(numbers, "",visited,prime)
    return len(answer)

#print(solution("17"))