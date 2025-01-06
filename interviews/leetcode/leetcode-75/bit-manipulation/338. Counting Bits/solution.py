class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)

        # Loop through all numbers from 1 to n
        for i in range(1, n + 1):
            # If i is even, dp[i] = dp[i // 2]
            # If i is odd, dp[i] = dp[i // 2] + 1
            dp[i] = dp[i >> 1] + (i & 1)

        return dp

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     n = 5
#     print(solution.countBits(n))  # Output: [0, 1, 1, 2, 1, 2]
