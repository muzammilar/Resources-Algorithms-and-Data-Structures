# Define the TreeNode class to structure the binary tree nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If root is None or root's value equals the target value, return the root
        if root is None or root.val == val:
            return root

        # If the target value is less than the root's value, search the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)

        # If the target value is greater than the root's value, search the right subtree
        return self.searchBST(root.right, val)

# Uncomment to test the function
# if __name__ == "__main__":
#     root = TreeNode(4)
#     root.left = TreeNode(2)
#     root.right = TreeNode(7)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(3)
#     solution = Solution()
#     result = solution.searchBST(root, 2)
#     print(result.val)  # Expected Output: 2
