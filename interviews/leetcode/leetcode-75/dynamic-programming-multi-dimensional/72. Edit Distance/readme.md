### 72. Edit Distance

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have the following three operations permitted:

- Insert a character.
- Delete a character.
- Replace a character.

##### Example:

Input:
`word1 = "horse"`,
`word2 = "ros"`
Output:
`3`
Explanation:
The minimum number of operations required to convert "horse" to "ros" is:
- "horse" → "ros" by performing the following operations:
    1. "horse" → "rorse" by replacing 'h' with 'r'
    2. "rorse" → "ros" by deleting 'r'
    3. "ros" → "ros" by deleting 'e'

---

#### Approach:

This problem can be solved using **Dynamic Programming (DP)**.

1. **Define DP State**:
   Let `dp[i][j]` represent the minimum number of operations needed to convert the first `i` characters of `word1` to the first `j` characters of `word2`.

2. **Base Case**:
   - If either string is empty:
     - `dp[i][0] = i` for all `0 <= i <= len(word1)`: This is because we need to delete all characters from `word1` to match an empty `word2`.
     - `dp[0][j] = j` for all `0 <= j <= len(word2)`: This is because we need to insert all characters into `word1` to match `word2`.

3. **Recurrence Relation**:
   - If `word1[i-1] == word2[j-1]`, no operation is needed:
     `dp[i][j] = dp[i-1][j-1]`
   - If `word1[i-1] != word2[j-1]`, we have three possible operations:
     - **Insert** a character to `word1`: `dp[i][j] = dp[i][j-1] + 1`
     - **Delete** a character from `word1`: `dp[i][j] = dp[i-1][j] + 1`
     - **Replace** a character in `word1`: `dp[i][j] = dp[i-1][j-1] + 1`

   We take the minimum of these three options:

   ```
   dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
   ```

4. **Space Optimization**:
- Instead of using a 2D array, we can optimize the space by using only two 1D arrays (previous and current rows), since each row only depends on the previous row.

---

#### Time Complexity:
- **O(m * n)**: We need to iterate through each cell in the `dp` table, where `m` and `n` are the lengths of `word1` and `word2`, respectively.

#### Space Complexity:
- **O(min(m, n))**: We can optimize space by using only two 1D arrays instead of a 2D array.
