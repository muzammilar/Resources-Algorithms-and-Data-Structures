class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Pointer to track position of the next non-zero element
        non_zero_index = 0

        # Iterate through the array
        for i, _ in enumerate(nums):
            if nums[i] != 0:
                # Swap non-zero element to the front
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1
