class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0  # start this pointer from the left side
        right = len(height) - 1 # start this pointer from the right side
        max_area = 0

        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area
            max_area = max(max_area, current_area)

            # Move the pointer for the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
