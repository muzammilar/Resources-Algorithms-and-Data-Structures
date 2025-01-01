### 437. Path Sum III

You are given a binary tree where each node has a value. You are also given an integer `targetSum`. You need to find the number of paths in the tree that sum to `targetSum`. The path does not need to start at the root or end at a leaf, but it must go downwards (meaning that it must be a contiguous path within the tree).

#### Explanation of the Algorithm:

1. **Prefix Sum**: The main idea is to maintain a running sum of node values (`current_sum`). For each node, we calculate `current_sum - target` and check if this value exists in the prefix sum map. If it does, it means there exists a path (from an ancestor to the current node) that sums up to the target.

2. **Hash Map**: We store the count of prefix sums in the hash map. This allows us to quickly check how many times a particular cumulative sum has occurred. The value of `current_sum - target` in the map indicates that there exists a subarray whose sum equals `target`.

3. **Backtracking**: After visiting a node and processing its left and right subtrees, we backtrack by decrementing the count of the current sum in the map, as the current path is no longer valid for subsequent nodes.

---

#### Time Complexity:

- **O(n)**, where `n` is the number of nodes in the tree. Each node is visited once during the DFS traversal.

#### Space Complexity:

- **O(n)**, due to the space used by the hash map and the recursion stack. In the worst case, the recursion stack can go as deep as the height of the tree (which can be `O(n)` in the case of a skewed tree), and the hash map stores at most `O(n)` different cumulative sums.

---
