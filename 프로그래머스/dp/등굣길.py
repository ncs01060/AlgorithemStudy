def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)] 
    dp[0][0] = 1

    for i in range(0,n):
        for j in range(0,m):
            if i == 0 and j == 0:
                continue
            elif [j+1,i+1] in puddles:
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    return dp[n-1][m-1]

print(solution(4,3,[[2, 2]]))
print(solution(3,3,[[2, 1]]))
print(solution(3,3,[[2, 3]]))
print(solution(3,3,[[2, 2]]))
print(solution(4,5,[[1, 2], [2, 2], [3, 2], [2, 4], [3, 4], [4, 4]]))
print(solution(4,3,[[2, 1]]))