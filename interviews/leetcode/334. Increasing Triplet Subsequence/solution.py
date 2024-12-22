class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')  # Initialize the first smallest element
        second = float('inf') # Initialize the second smallest element

        for num in nums:
            if num <= first:       # Update first if num is smaller
                first = num
            elif num <= second:    # Update second if num is larger than first but smaller than second
                second = num
            else:                  # If we find a num larger than both, we have a triplet
                return True
        return False
