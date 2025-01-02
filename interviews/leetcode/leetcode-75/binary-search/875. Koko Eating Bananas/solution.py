import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Helper function to calculate hours needed at speed k
        def hours_needed(k):
            return sum(math.ceil(pile / k) for pile in piles)

        # Binary search for the minimum speed
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid  # Try smaller speeds
            else:
                left = mid + 1  # Need a larger speed

        return left

# Main function (commented out by default)
# if __name__ == "__main__":
#     solution = Solution()
#     piles = [3, 6, 7, 11]
#     h = 8
#     print(solution.minEatingSpeed(piles, h))  # Expected output: 4
