### 700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and a value `val`. You need to find the node in the BST that contains the value `val` and return the node. If the value is not found, return `null`.

#### Explanation:
- The node with value 2 exists in the tree. It has a left child with value 1 and a right child with value 3.

#### Approach:

We use the **binary search tree property** to efficiently search for the value:
1. If the current node’s value matches the target value, return the node.
2. If the target value is smaller than the node's value, recursively search the left subtree.
3. If the target value is larger, recursively search the right subtree.

#### Time Complexity:
- **O(h)** where `h` is the height of the tree. In the worst case, this is O(n) if the tree is skewed, or O(log n) if the tree is balanced.

#### Space Complexity:
- **O(h)** where `h` is the height of the tree. This accounts for the recursion stack. In the worst case, it can be O(n), and in the best case (balanced tree), it is O(log n).
