### 435. Non-overlapping Intervals

### Problem Statement:

Given a collection of intervals, find the minimum number of intervals you need to remove so that the remaining intervals do not overlap.

- Implement the following method:
  - `eraseOverlapIntervals(intervals: List[List[int]]) -> int`: Given a list of `intervals`, return the minimum number of intervals that need to be removed so that the remaining intervals do not overlap.

#### Approach:

1. **Sort Intervals by Ending Time**: Start by sorting the intervals by their ending time. This is because, when choosing which intervals to keep, it is optimal to keep the one with the earliest end time, as it leaves the most room for the next interval.

2. **Greedy Algorithm**: After sorting, iterate through the intervals and keep track of the last added interval. If the current interval starts after or at the end of the last interval, it does not overlap, so we keep it. Otherwise, we need to remove the current interval.

3. **Count Removals**: The number of intervals that need to be removed is simply the number of times we encounter an overlap.

#### Time Complexity:
- Sorting the intervals: O(n * log n), where `n` is the number of intervals.
- Iterating through the intervals: O(n).

Thus, the overall time complexity is O(n * log n).

#### Space Complexity:
- O(1) extra space, as we are modifying the input intervals in-place and using a few variables.
