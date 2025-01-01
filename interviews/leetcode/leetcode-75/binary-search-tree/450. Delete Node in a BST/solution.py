# Define the TreeNode class to structure the binary tree nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If root is None, return None
        if not root:
            return None

        # If the value is smaller than root's value, move to the left subtree
        if val < root.val:
            root.left = self.deleteNode(root.left, val)
        # If the value is greater than root's value, move to the right subtree
        elif val > root.val:
            root.right = self.deleteNode(root.right, val)
        # If the value is equal to root's value, this is the node to delete
        else:
            # Case 1: Node has no children (leaf node)
            if not root.left and not root.right:
                root = None
            # Case 2: Node has one child
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            # Case 3: Node has two children
            else:
                # Find the in-order successor (smallest in the right subtree)
                successor = self._findMin(root.right)
                # Replace the node's value with the in-order successor's value
                root.val = successor.val
                # Delete the in-order successor
                root.right = self.deleteNode(root.right, successor.val)

        return root

    def _findMin(self, node: TreeNode) -> TreeNode:
        # Find the node with the minimum value (leftmost node)
        while node.left:
            node = node.left
        return node

# Uncomment to test the function
# if __name__ == "__main__":
#     root = TreeNode(5)
#     root.left = TreeNode(3)
#     root.right = TreeNode(6)
#     root.left.left = TreeNode(2)
#     root.left.right = TreeNode(4)
#     root.right.right = TreeNode(7)
#     solution = Solution()
#     result = solution.deleteNode(root, 3)
#     print(result.val)  # Expected Output: 5 (the new root after deletion)
