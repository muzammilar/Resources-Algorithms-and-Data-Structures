
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        count = 0
        last_end = intervals[0][1]

        # Iterate through the intervals and count the removals
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                # If the current interval overlaps with the last one, increment count
                count += 1
            else:
                # Update last_end to be the end of the current interval
                last_end = intervals[i][1]

        return count

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
#     result = solution.eraseOverlapIntervals(intervals)
#     print(result)  # Output: 1
