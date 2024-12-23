class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # keep two pointers with a dynamic sliding window
        left = 0
        max_length = 0
        zero_count = 0

        # Sliding window approach
        for right, _ in enumerate(nums):
            if nums[right] == 0:
                zero_count += 1

            # If there are more than 'k' zeros, move the left pointer
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the maximum length of window with at most 'k' zeros
            max_length = max(max_length, right - left + 1)

        return max_length
