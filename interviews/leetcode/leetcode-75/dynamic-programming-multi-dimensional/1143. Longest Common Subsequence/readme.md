### 1143. Longest Common Subsequence

Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

A **subsequence** is different from a **substring**. A substring is a contiguous sequence of characters, while a subsequence is not necessarily contiguous.

##### Example:

Input:
`text1 = "abcde", text2 = "ace"`
Output:
`3`
Explanation:
The longest common subsequence is `"ace"`, which has length `3`.

---

#### Approach:

This problem can be solved using **Dynamic Programming (DP)**.

1. **Define DP State**:
   Let `dp[i][j]` represent the length of the longest common subsequence between the first `i` characters of `text1` and the first `j` characters of `text2`.

2. **Base Case**:
   - If either string is empty (i.e., `i = 0` or `j = 0`), the length of the longest common subsequence is `0`. Therefore, for all `i`, `dp[i][0] = 0`, and for all `j`, `dp[0][j] = 0`.

3. **Recurrence Relation**:
   - If `text1[i-1] == text2[j-1]`, then `dp[i][j] = dp[i-1][j-1] + 1`. This is because the current characters match, so we can extend the subsequence.
   - If `text1[i-1] != text2[j-1]`, then `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`. This means we either skip the current character of `text1` or `text2`, and take the maximum of the two possibilities.

4. **Space Optimization**:
   - Instead of using a 2D array for the entire `dp` table, we can optimize space by keeping only two 1D arrays (previous and current rows), since each row only depends on the previous row.

---

#### Time Complexity:
- **O(m * n)**: We need to iterate through each character of both strings to fill the `dp` table, where `m` and `n` are the lengths of `text1` and `text2`, respectively.

#### Space Complexity:
- **O(min(m, n))**: We can optimize the space complexity by using only two 1D arrays instead of a 2D array.
