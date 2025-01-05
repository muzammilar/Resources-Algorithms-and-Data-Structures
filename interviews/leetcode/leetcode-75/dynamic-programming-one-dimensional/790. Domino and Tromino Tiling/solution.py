class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # Edge cases for n == 0 or n == 1 or n == 2
        if n == 0 or n == 1 or n == 2:
            return n

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2*dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     n = 3
#     print(solution.numTilings(n))  # Output: 5
