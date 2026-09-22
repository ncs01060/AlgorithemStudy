def solution(n):
    answer = bin(n).count("1")
    num = n + 1
    
    while True:
        if answer == bin(num).count("1"):
            answer = num
            break
        num += 1
    
    
    return answer