class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        max_length = 0
        zero_count = 0

        # Sliding window approach
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # If there are more than one '0's, shrink the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the maximum length of the subarray with at most one '0'
            max_length = max(max_length, right - left + 1)

        # If the entire array consists of 1's, the result should be n-1 (since we must delete one element)
        return max_length - 1 if max_length == len(nums) else max_length
