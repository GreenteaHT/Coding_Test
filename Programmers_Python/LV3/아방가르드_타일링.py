def solution(n):
    MOD = 1000000007
    dp = [1, 1, 3, 10] + [0] * (n)
    
    for i in range(4, n + 1):
        dp[i] = (dp[i-1] + 2*dp[i-2] + 6*dp[i-3] + dp[i-4] - dp[i-6]) % MOD
            
    return dp[n]

# 입출력 예시
print(solution(2))
print(solution(5))
