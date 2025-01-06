### 62. Unique Paths

A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

##### Example:

Input: `m = 3, n = 7`
Output: `28`
Explanation: There are 28 unique paths to go from the top-left to the bottom-right corner.

---

#### Approach:

This problem can be approached using **Dynamic Programming (DP)**.

1. **Define DP State**:
   Let `dp[i][j]` represent the number of ways to reach the cell at position `(i, j)` from the top-left corner `(0, 0)`.

2. **Base Case**:
   - There's only one way to get to any cell in the first row, which is by moving right continuously. Thus, for all `dp[0][j] = 1` for `0 <= j < n`.
   - Similarly, there's only one way to get to any cell in the first column, which is by moving down continuously. Thus, for all `dp[i][0] = 1` for `0 <= i < m`.

3. **Recurrence Relation**:
   For any other cell `(i, j)`, the number of ways to reach it can be obtained by the sum of the number of ways to reach the cell directly above it `(i-1, j)` and the cell directly to its left `(i, j-1)`. Thus:

   ```
   dp[i][j] = dp[i-1][j] + dp[i][j-1]
   ```

This equation works because the robot can only move either down or right, so the total number of ways to reach a given cell is the sum of the ways to reach its neighboring cells.

4. **Space Optimization**:
- Instead of using a `m x n` grid, we can optimize space by keeping only the current row of the grid, since each cell only depends on the cell in the current row and the previous row.

---

#### Time Complexity:
- **O(m * n)**: We need to iterate through each cell in the grid to compute the number of ways to reach it.

#### Space Complexity:
- **O(n)**: We can optimize space by using only a 1D array to store the results for the current row.
