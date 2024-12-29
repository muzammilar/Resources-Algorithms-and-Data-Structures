class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}  # Initialize with 0 to handle the case when a subarray starts from the beginning
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum_count:
                result += prefix_sum_count[current_sum - k]
            # Update the map with the current cumulative sum
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return result

# The main function is commented by default.
# solution = Solution()
# nums = [1, 1, 1]
# k = 2
# print(solution.subarraySum(nums, k))  # Output: 2
