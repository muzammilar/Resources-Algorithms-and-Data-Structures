class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Base case: if root is None or root is one of the nodes
        if not root or root == p or root == q:
            return root

        # Recursively search for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different subtrees, root is their LCA
        if left and right:
            return root

        # Otherwise, return the non-null child (either left or right)
        return left if left else right
