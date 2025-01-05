### 746. Min Cost Climbing Stairs

You are given an integer array `cost` where `cost[i]` is the cost of stepping on the `i`-th stair. Once you pay the cost, you can either:
- Jump to the next stair, `i + 1`, or
- Jump to the stair after the next, `i + 2`.

You need to find the minimum cost to reach the top of the floor, which is beyond the last stair. You can either start at stair `0` or stair `1`.

#### Approach:

This problem can be solved using dynamic programming. The idea is to maintain an array `dp` where `dp[i]` represents the minimum cost to reach the `i`-th stair. The recurrence relation is:

- `dp[i] = min(dp[i-1], dp[i-2]) + cost[i]` for `i >= 2`
- Base cases:
  - `dp[0] = cost[0]`
  - `dp[1] = cost[1]`

Finally, the minimum cost to reach the top of the floor will be the minimum of the last two entries `dp[len(cost) - 1]` and `dp[len(cost) - 2]`, as we can jump from either of these stairs.

#### Time Complexity:
- The time complexity is **O(n)** where `n` is the length of the `cost` array, as we only iterate through the array once.

#### Space Complexity:
- The space complexity is **O(n)** for storing the dynamic programming table. However, we can optimize this to **O(1)** if we only store the last two computed values.
