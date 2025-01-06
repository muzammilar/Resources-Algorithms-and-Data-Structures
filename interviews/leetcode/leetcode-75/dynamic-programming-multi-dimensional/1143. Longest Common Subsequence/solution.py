class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Use two 1D arrays for space optimization
        dpPrev = [0] * (n + 1)
        dpCurr = [0] * (n + 1)

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dpCurr[j] = dpPrev[j - 1] + 1
                else:
                    dpCurr[j] = max(dpPrev[j], dpCurr[j - 1])

            # Swap the current and previous row
            dpPrev, dpCurr = dpCurr, dpPrev

        return dpPrev[n]

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     text1 = "abcde"
#     text2 = "ace"
#     print(solution.longestCommonSubsequence(text1, text2))  # Output: 3
