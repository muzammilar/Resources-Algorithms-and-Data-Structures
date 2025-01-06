class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 1D array to store the number of unique paths for each cell in a row
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]  # dp[j] is the sum of the number of ways to move from the left and from above

        return dp[-1]  # The last element contains the number of unique paths to the bottom-right corner

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     m, n = 3, 7
#     print(solution.uniquePaths(m, n))  # Output: 28
