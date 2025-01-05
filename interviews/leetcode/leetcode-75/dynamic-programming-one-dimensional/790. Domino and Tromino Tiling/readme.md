### 790. Domino and Tromino Tiling

You have a 2 x n board and you want to cover it with the following tiles:
- A **domino** tile of size 2 x 1.
- A **tromino** tile of size 2 x 2, shaped like an "L".

Return the number of ways to tile the board. Since the answer may be very large, return it modulo 10^9 + 7.

##### Example:
Input: `n = 3`
Output: `5`
Explanation:
The five possible ways are:
- 3 dominoes
- 1 tromino + 1 domino
- 1 domino + 1 tromino
- 2 trominos

---

#### Approach:

This problem can be solved using **Dynamic Programming (DP)**.

Let `dp[i]` represent the number of ways to tile a 2 x i board. We can establish the following recurrence relations:

1. **Base Cases**:
   - `dp[0] = 1`: There is one way to tile a 2 x 0 board (by not placing any tiles).
   - `dp[1] = 1`: There is one way to tile a 2 x 1 board (using one domino).
   - `dp[2] = 2`: There are two ways to tile a 2 x 2 board (either two dominoes or one tromino).

2. **Recurrence Relation**:
   For `i >= 3`, the number of ways to tile a 2 x i board can be computed as:
   - `dp[i] = 2 * dp[i-1]  + dp[i-3]`
     - `2 * dp[i-1]` accounts for adding one domino (a 2x1 tile).
     - `dp[i-2]` accounts for adding two dominoes.
     - `2 * dp[i-3]` accounts for adding one tromino, which can be placed in two distinct ways: either in the first row or in the second row.

3. **Modulo Operation**:
   Since the result could be large, every operation is taken modulo \(10^9 + 7\).


#### Time Complexity:
- **O(n)**: We only need to compute `dp[i]` for `i = 0` to `n`, which requires linear time.

#### Space Complexity:
- **O(n)**: We store the results for all values of `i` from 0 to `n`.
