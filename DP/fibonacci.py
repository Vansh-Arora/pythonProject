def helper(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1: return dp[n]
    dp[n] = helper(n - 1, dp) + helper(n - 2, dp)
    return dp[n]

def fibo(n):
    dp = [-1 for _ in range(n+1)]
    return helper(n, dp)



if __name__ == "__main__":
    n = 5
    for i in range(n):
        print(fibo(i))