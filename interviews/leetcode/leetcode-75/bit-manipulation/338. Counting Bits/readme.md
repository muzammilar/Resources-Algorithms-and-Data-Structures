### 338. Counting Bits

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (where `0 <= i <= n`), `ans[i]` is the number of `1` bits in the binary representation of `i`.

##### Example:

Input:
`n = 5`
Output:
`[0, 1, 1, 2, 1, 2]`
Explanation:
- `0` in binary is `0` → 0 one bits
- `1` in binary is `1` → 1 one bit
- `2` in binary is `10` → 1 one bit
- `3` in binary is `11` → 2 one bits
- `4` in binary is `100` → 1 one bit
- `5` in binary is `101` → 2 one bits

---

#### Approach:

This problem can be solved efficiently using a **Dynamic Programming (DP)** approach.

1. **Key Insight**:
   The number of `1` bits in a number `i` can be related to the number of `1` bits in `i >> 1` (which is `i` divided by 2) because the binary representation of `i` is essentially the binary representation of `i >> 1` with the last bit added. Specifically, if `i` is even, the number of `1` bits in `i` is the same as the number of `1` bits in `i >> 1`. If `i` is odd, the number of `1` bits in `i` is one more than the number of `1` bits in `i >> 1`.

2. **Dynamic Programming Recurrence**:
   - If `i` is even:
     `dp[i] = dp[i // 2]` (because no additional bit is added).
   - If `i` is odd:
     `dp[i] = dp[i // 2] + 1` (because the last bit is 1).

3. **Space Optimization**:
   - We can use an array `dp` of size `n + 1` where `dp[i]` stores the number of `1` bits for the number `i`.

---

#### Time Complexity:
- **O(n)**: We iterate through all numbers from `0` to `n`, and for each number, we only perform constant time operations.

#### Space Complexity:
- **O(n)**: We store the results for all numbers from `0` to `n` in the array `dp`.
