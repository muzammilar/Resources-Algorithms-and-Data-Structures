class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Initialize two variables to keep track of the previous two max values
        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
        current = prev2

        # Loop through the array starting from the third house
        for i in range(2, len(nums)):
            current = max(prev2, nums[i] + prev1)
            prev1 = prev2
            prev2 = current

        return current

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     nums = [2, 3, 2]
#     print(solution.rob(nums))  # Output: 3
