### 1318. Minimum Flips to Make a OR b Equal to c

Given three integers `a`, `b`, and `c`, return the minimum number of flips required to make `a` OR ` b` equal to `c`.

In one flip, you can change any bit of `a` or `b` from `1` to `0` or from `0` to `1`.

##### Example:

Input:
`a = 2`, `b = 6`, `c = 5`
Output:
`3`
Explanation:
- Binary representation of `a = 2` → `010`
- Binary representation of `b = 6` → `110`
- Binary representation of `c = 5` → `101`
- To make `a | b = c`, we need 3 flips:
    1. Flip the second bit of `a` from `1` to `0` (since `a` has 010 and `c` has 101).
    2. Flip the first bit of `b` from `1` to `0` (since `b` has 110 and `c` has 101).
    3. Flip the second bit of `b` from `1` to `0` (since `b` has 110 and `c` has 101).

#### Approach:

To solve this problem efficiently, we will use a **bit manipulation** approach.

1. **Bitwise OR**:
   The OR operation between two bits returns `1` if either of the bits is `1`.
   Therefore, we need to compare the bits of `a`, `b`, and `c` at each position and decide whether we need to flip any bits in `a` or `b`.

2. **Steps to Minimize the Flips**:
   - For each bit position from `0` to `31` (assuming 32-bit integers), compare the corresponding bits in `a`, `b`, and `c`:
     - If the bit in `c` is `0`, both `a` and `b` must have `0` at that position. If either has `1`, we need to flip it.
     - If the bit in `c` is `1`, we need at least one of the corresponding bits in `a` or `b` to be `1`. If both are `0`, we must flip one of them.

3. **Count the Flips**:
   Count the total flips needed for all the bit positions.

---

#### Time Complexity:
- **O(1)**: Since we only need to iterate through 32 bit positions (assuming 32-bit integers), this solution runs in constant time.

#### Space Complexity:
- **O(1)**: We only use a constant amount of space.
