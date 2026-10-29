def solution(money):
    dp = [0] * 1000001
    dp2 = [0] * 1000001
    dp[0] = money[0]
    dp[1] = money[0]
    
    for i in range(2,len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    dp2[0] =0
    dp2[1] = money[1]
    
    for i in range(2,len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    # print(dp[1])
    # print(dp2[1])
    
    return max(max(dp2), max(dp))


print(solution([1, 2, 3, 1]))
print(solution([3,2,1]))