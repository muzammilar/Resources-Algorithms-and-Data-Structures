class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Use two 1D arrays for space optimization
        dpPrev = [0] * (n + 1)
        dpCurr = [0] * (n + 1)

        # Initialize the base cases
        for j in range(n + 1):
            dpPrev[j] = j

        # Fill the dp table
        for i in range(1, m + 1):
            dpCurr[0] = i  # base case for dp[i][0]
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dpCurr[j] = dpPrev[j - 1]  # no operation needed
                else:
                    dpCurr[j] = min(dpPrev[j-1], dpPrev[j], dpCurr[j-1]) + 1

            # Swap the current and previous rows
            dpPrev, dpCurr = dpCurr, dpPrev

        return dpPrev[n]

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     word1 = "horse"
#     word2 = "ros"
#     print(solution.minDistance(word1, word2))  # Output: 3
