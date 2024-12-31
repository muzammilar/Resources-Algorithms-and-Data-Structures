### 450. Delete Node in a BST

Given the root of a binary search tree (BST) and a node’s value, delete the node from the BST. Ensure that the deletion follows the BST property.

#### Approach:

1. Traverse the tree to find the node with the value to delete.
2. If the node has:
   - **No children:** Remove the node.
   - **One child:** Replace the node with its child.
   - **Two children:** Replace the node's value with the in-order successor's value and delete the successor.

#### Time Complexity:
- **O(h)** where `h` is the height of the tree. In the worst case (unbalanced tree), it is O(n), and in the best case (balanced tree), it is O(log n).

#### Space Complexity:
- **O(h)** where `h` is the height of the tree. This accounts for the recursion stack. In the worst case, it is O(n), and in the best case, it is O(log n).
