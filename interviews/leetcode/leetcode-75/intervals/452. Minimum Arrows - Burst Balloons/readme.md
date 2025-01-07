### 452. Minimum Number of Arrows to Burst Balloons

There are `n` balloons, represented by intervals `balloons[i] = [xstart, xend]`, where `xstart` is the start point and `xend` is the end point. You are tasked with finding the minimum number of arrows that must be shot to burst all the balloons.

- Implement the following method:
  - `findMinArrowShots(intervals: List[List[int]]) -> int`: Given a list of `intervals` representing balloons, return the minimum number of arrows that must be shot to burst all the balloons.

#### Approach:

1. **Sort by Ending Time**: Start by sorting the intervals by their end time. This allows us to take a greedy approach, where we can burst as many balloons as possible with one arrow.

2. **Greedy Approach**: After sorting, iterate through the intervals and check if the current balloon overlaps with the previous one (i.e., the start of the current balloon is less than or equal to the end of the previous balloon). If it does, they can be burst with the same arrow, so we continue. Otherwise, a new arrow is needed, and we update the arrow count.

3. **Count Arrows**: The final answer will be the total number of arrows used to burst all balloons.

#### Time Complexity:
- Sorting the intervals: O(n * log n), where `n` is the number of intervals.
- Iterating through the intervals: O(n).

Thus, the overall time complexity is O(n * log n).

#### Space Complexity:
- O(1) extra space as we only need a few variables to keep track of the arrows and current balloon positions.
