### 216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that:

- Only numbers 1 through 9 are allowed.
- Each combination should be a unique set of numbers.

Return a list of all unique combinations of k numbers that sum up to n.

Note:
- The solution set must not contain duplicate combinations.
- The combinations should be sorted in ascending order.

---

#### Approach:

1. **Backtracking Approach**:
   - The problem is a combination problem where we need to select `k` distinct numbers that sum up to `n` from the set {1, 2, ..., 9}.
   - We will use backtracking to explore all possible combinations.
   - Start from 1 and recursively add numbers to a combination, ensuring that the sum doesn’t exceed `n`.
   - At each step, if the combination length reaches `k` and the sum matches `n`, we store the combination.
   - If the sum exceeds `n` or the combination length exceeds `k`, we backtrack.

2. **Backtracking Explanation**:
   - We iterate through numbers from `1` to `9`, attempting to add each number to the current combination.
   - If the sum of the current combination is less than `n` and the length is less than `k`, we continue exploring further.
   - Once a valid combination (of size `k` and sum `n`) is found, it is added to the result.

#### Time Complexity:

The time complexity is O(C(9, k)), where C(9, k) is the number of combinations of k elements chosen from 9. In the worst case, the solution explores all combinations of `k` elements from the set of 9 numbers.

#### Space Complexity:

The space complexity is O(k), where `k` is the maximum size of a combination. This is because t
