class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        # XOR all elements in the array
        for num in nums:
            res ^= num
        return res

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     nums = [4, 1, 2, 1, 2]
#     print(solution.singleNumber(nums))  # Output: 4
