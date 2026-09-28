def solution(n, times):
    answer = 0
    left = 0
    right = n * max(times)
    
    
    while left < right:
        time = 0
        mid = (left + right) // 2
        
        for i in times:
            time += mid // i
        
        
        if time >= n:
            right = mid
        elif time <= n:
            left = mid + 1

            
    
    return left