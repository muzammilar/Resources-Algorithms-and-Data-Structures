### 198. House Robber

You are a robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing two adjacent houses is that the police are always watching you. After robbing a house, you cannot rob the next house directly. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

#### Example:
Input: `nums = [2, 3, 2]`
Output: `3`
Explanation: You cannot rob house 0 and house 2 because they are adjacent to each other. So, the maximum you can rob is `3`.

---

#### Approach:

1. **Dynamic Programming Approach**:
   - If you rob a house, you cannot rob the next house. This can be modeled as a decision between robbing the current house and skipping the next one or skipping the current house and continuing with the next one.
   - Let `dp[i]` represent the maximum amount of money you can rob from house 0 to house `i`.
   - The recurrence relation will be:
     ```
     dp[i] = max(dp[i-1], nums[i] + dp[i-2])
     ```
   - Base cases:
     - `dp[0] = nums[0]` (First house)
     - `dp[1] = max(nums[0], nums[1])` (Maximum of robbing the first or the second house)

   This approach ensures we are making the optimal decision at each house.

2. **Edge Cases**:
   - If the list is empty, return `0` because there are no houses to rob.
   - If there is only one house, return the amount of money in that house.

---

#### Time Complexity:
- **O(n)**: We only iterate through the array once.

#### Space Complexity:
- **O(1)**: We can optimize the space by storing only the last two `dp` values instead of the whole array.
