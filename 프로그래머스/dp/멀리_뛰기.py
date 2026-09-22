def solution(n):
    answer = 0
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(3,n+1):
        dp[i] = (dp[i-2] + dp[i-1]) 
        
        
        
    
    return dp[n] % 1234567