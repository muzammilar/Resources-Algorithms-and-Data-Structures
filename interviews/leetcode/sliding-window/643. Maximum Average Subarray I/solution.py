class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1: Calculate the sum of the first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Use sliding window to find the maximum sum of subarrays of length k
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # Add the new element, subtract the old one
            max_sum = max(max_sum, window_sum)

        # Step 3: Return the maximum average
        return max_sum / k
