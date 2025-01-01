# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Get the leaf nodes for both trees
        leaves1 = getLeaves(root1)
        leaves2 = getLeaves(root2)

        # Compare the leaf nodes
        return leaves1 == leaves2

        # Helper function to collect the leaf nodes in a tree
def getLeaves(root):
    leaves = []
    if not root:
        return leaves
    # If it's a leaf node, add it to the list
    if not root.left and not root.right:
        leaves.append(root.val)
    # Recurse for left and right children
    leaves.extend(getLeaves(root.left))
    leaves.extend(getLeaves(root.right))
    return leaves


# Helper function to create a binary tree from a list (for testing purposes)
def create_binary_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

# Test the solution
# if __name__ == "__main__":
#     solution = Solution()
#     root1 = create_binary_tree([3,5,1,6,2,9,8,None,None,7,4])
#     root2 = create_binary_tree([3,5,1,6,7,4,2,None,None,None,None,9,8])
#     result = solution.leafSimilar(root1, root2)
#     print(result)  # Output: True
