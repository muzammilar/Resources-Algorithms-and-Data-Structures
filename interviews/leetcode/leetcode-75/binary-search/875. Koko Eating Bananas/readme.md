### 875. Koko Eating Bananas


Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. Koko can choose any pile of bananas and eat `k` bananas from it. However, Koko can only eat at a speed of `k` bananas per hour.

Koko wants to eat all the bananas within `h` hours. The task is to return the minimum integer `k` such that Koko can eat all the bananas in `h` hours.

**Note**:
- You cannot eat fractional bananas, and you must eat at least one banana from a pile each time you pick a pile to eat from.

---

#### Approach

The problem is asking for the minimum speed `k` such that Koko can eat all the bananas within `h` hours. Here's how we can solve this efficiently:

1. **Binary Search**:
   - **Lower Bound**: The minimum speed `k` must be at least 1 because Koko must eat at least 1 banana per hour.
   - **Upper Bound**: The maximum speed `k` is the size of the largest pile, as Koko could eat the entire pile in one hour if she eats at the maximum speed.

2. **Checking Feasibility**:
   - For each speed `k` between the lower and upper bounds, calculate how many hours Koko would need to eat all bananas at that speed.
   - For a pile of size `piles[i]`, the time required to eat all bananas from that pile is `ceil(piles[i] / k)`.
   - Sum up the hours for all piles and check if it's less than or equal to `h`.

3. **Binary Search Process**:
   - Perform binary search between `1` and the maximum number of bananas in any pile.
   - If the total hours are less than or equal to `h` at speed `k`, try smaller speeds (i.e., move left in the binary search).
   - If the total hours exceed `h`, try larger speeds (i.e., move right in the binary search).

This ensures that we find the smallest `k` that satisfies the condition.

#### Time Complexity

- **Time Complexity**: **O(n * log(max(piles)))**
  The binary search operates in **O(log(max(piles)))** time, and for each speed `k`, we calculate the total hours needed in **O(n)** time, where `n` is the number of piles. Therefore, the total complexity is **O(n * log(max(piles)))**.

#### Space Complexity

- **Space Complexity**: **O(1)**
  We only use a constant amount of space to store variables for the binary search bounds and to compute the total hours. Hence, the space complexity is constant.
