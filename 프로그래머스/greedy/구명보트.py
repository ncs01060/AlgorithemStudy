def solution(people, limit):
    answer = 0
    people.sort()
    pointer1 = 0
    pointer2 = len(people) - 1
    
    while pointer1 <= pointer2:
        if people[pointer1] + people[pointer2] <= limit:
            pointer1 += 1
        pointer2 -= 1
        answer += 1
    
    
    return answer