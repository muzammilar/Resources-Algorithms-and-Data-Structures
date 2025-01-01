### 1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, find the level with the maximum sum of node values. Return the **1-based index** of that level.

#### Explanation:
- Level 1: 1
- Level 2: 2 + 3 = 5
- Level 3: 4 + 5 + 6 = 15

The maximum sum is 15 at level 3, so the output is 3.

#### Approach:

We use **Breadth-First Search (BFS)** to traverse the binary tree level by level, calculating the sum of nodes at each level. We track the level with the maximum sum.

#### Time Complexity:
- **O(n)** where `n` is the number of nodes in the binary tree.

#### Space Complexity:
- **O(n)** where `n` is the number of nodes. This accounts for the space used by the queue during BFS traversal.
