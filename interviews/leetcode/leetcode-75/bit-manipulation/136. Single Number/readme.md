### 136. Single Number

### Problem Statement:

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution that runs in linear time and uses only constant extra space.

##### Example:

Input:
`nums = [2, 2, 1]`
Output:
`1`

Input:
`nums = [4, 1, 2, 1, 2]`
Output:
`4`

#### Approach:

This problem can be efficiently solved using the **XOR operation**.

1. **XOR Properties**:
   - `a ^ a = 0`: XOR of a number with itself is `0`.
   - `a ^ 0 = a`: XOR of a number with `0` is the number itself.
   - XOR is **commutative** and **associative**: The order in which you apply XOR does not affect the result.

2. **Key Insight**:
   - Since all numbers appear twice except one, applying XOR to all the numbers will cancel out the numbers that appear twice (because `a ^ a = 0`).
   - The only number that does not get canceled out is the number that appears once.

3. **Algorithm**:
   - Initialize a variable `res` to `0`.
   - Loop through each number in the array and XOR it with `res`.
   - After the loop, `res` will contain the number that appears only once.

---

#### Time Complexity:
- **O(n)**: We iterate through the array once, where `n` is the length of the array.

#### Space Complexity:
- **O(1)**: We use only a constant amount of extra space for the `res` variable.
