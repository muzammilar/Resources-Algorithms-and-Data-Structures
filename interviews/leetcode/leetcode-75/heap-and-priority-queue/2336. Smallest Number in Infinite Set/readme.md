### 2336. Smallest Number in Infinite Set

You have an infinite set `S` = {1, 2, 3, 4, 5, 6, 7, ...}. You have a number `n` and you can remove any of its elements from the set `S`. For example, if `n = 2`, you remove the element `2` from the set `S`.

Your task is to implement the `SmallestInfiniteSet` class that will support the following operations:

##### 1. `addBack(n: int)`: Adds an integer `n` back into the infinite set if it was removed earlier. Otherwise, do nothing.
##### 2. `popSmallest() -> int`: Removes and returns the smallest integer from the infinite set.

#### Example:

```plaintext
Input:
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest"]
[[], [2], [], [], [1], [], []]

Output:
[null, null, 1, 2, null, 3, 4]
```

Explanation:
1. `SmallestInfiniteSet` initializes with the infinite set `S = {1, 2, 3, 4, 5, 6, 7, ...}`.
2. `addBack(2)` does nothing because 2 has already been removed from the set.
3. `popSmallest()` removes and returns the smallest element, which is 1.
4. `popSmallest()` removes and returns the smallest element, which is 2.
5. `addBack(1)` adds 1 back to the set.
6. `popSmallest()` removes and returns the smallest element, which is 3.
7. `popSmallest()` removes and returns the smallest element, which is 4.

##### Constraints:
- `1 <= n <= 1000`
- All numbers `n` will be unique.

---

#### Approach

The goal is to efficiently manage an infinite set while handling `popSmallest` and `addBack` operations.

##### 1. **Using a Set and Integer Tracking**:
We need two things:
1. **Set** to track the numbers that have been added back to the set after being removed.
2. **Integer tracking** to keep track of the smallest number that hasn't been used or removed yet.

#### Approach:
- We start by keeping track of the next smallest integer, initialized to `1`.
- When performing `popSmallest()`, we first check if there are any numbers in the "added back" set. If so, we return the smallest one.
- Otherwise, we return the `next` smallest integer and increment the next integer.
- The `addBack(n)` function simply adds `n` back to the set if it was previously removed.

#### Time Complexity:
- **addBack(n)**: **O(1)**, as we only need to add an element to a set.
- **popSmallest()**: **O(1)**, as we either pop from a set or increment a variable.

#### Space Complexity:
- **O(n)**, where `n` is the number of elements that have been added back to the set. This is the space used by the set.
