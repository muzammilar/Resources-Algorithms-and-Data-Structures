class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Find the peak element in the array using binary search approach.
        A peak element is one that is greater than its neighbors.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Check if mid is greater than both its neighbors
            if nums[mid] > nums[mid + 1]:
                # If so, the peak lies on the left side or at mid
                right = mid
            else:
                # Otherwise, the peak lies on the right side
                left = mid + 1

        # left == right, and that is the peak
        return left

# Main function (commented out by default)
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 2, 3, 1]
#     print(solution.findPeakElement(nums))  # Expected output: 2
