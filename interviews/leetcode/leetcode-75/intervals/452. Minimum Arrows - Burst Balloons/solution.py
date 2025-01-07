class Solution:
    def findMinArrowShots(self, intervals: list[list[int]]) -> int:
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        arrows = 1
        last_end = intervals[0][1]

        # Iterate through the intervals and count the number of arrows needed
        for i in range(1, len(intervals)):
            if intervals[i][0] > last_end:
                # If the current balloon doesn't overlap, a new arrow is needed
                arrows += 1
                last_end = intervals[i][1]

        return arrows

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     intervals = [[10, 16], [2, 8], [1, 6], [7, 12]]
#     result = solution.findMinArrowShots(intervals)
#     print(result)  # Output: 2
