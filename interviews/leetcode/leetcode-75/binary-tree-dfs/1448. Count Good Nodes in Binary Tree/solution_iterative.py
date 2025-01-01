# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Stack to store nodes and the max value encountered on the path
        stack = [(root, root.val)]
        count = 0

        while stack:
            node, max_val = stack.pop()

            # If the current node is a good node, increment the count
            if node.val >= max_val:
                count += 1

            # Update the max value for the path and add the children to the stack
            if node.left:
                stack.append((node.left, max(max_val, node.val)))
            if node.right:
                stack.append((node.right, max(max_val, node.val)))

        return count

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
#     root = create_binary_tree([3, 1, 4, 3, None, 1, 5])
#     result = solution.goodNodes(root)
#     print(result)  # Output: 4
