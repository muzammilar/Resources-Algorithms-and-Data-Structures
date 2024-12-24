class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0  # Initialize left sum to 0

        for i, num in enumerate(nums):
            # Calculate the right sum by subtracting left_sum and the current number
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum:
                return i  # Found the pivot index

            # Update left_sum for the next iteration
            left_sum += num

        return -1  # No pivot index found
