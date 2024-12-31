class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        left = 0
        max_length = 0
        zero_count = 0

        # Sliding window approach
        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1

            # If there are more than one '0's, shrink the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the maximum length of the subarray with at most one '0'
            max_length = max(max_length, right - left)  # We don't add +1 here since we already acciybt for one zero

        # return the maximum length
        return max_length
