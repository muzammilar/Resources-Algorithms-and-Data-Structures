from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is None, depth is 0
        if not root:
            return 0

        # Recursively find the max depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum of left and right depths, plus 1 for the current node
        return max(left_depth, right_depth) + 1


    # Bread first approach - iterative
    def maxDepthIterative(self, root: TreeNode) -> int:
        # Base case: if the tree is empty
        if not root:
            return 0

        # Initialize a queue for level order traversal
        queue = deque([root])
        depth = 0

        # Perform level order traversal
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)

            # Process all nodes at this level
            for _ in range(level_size):
                node = queue.popleft()

                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Increment depth after processing the current level
            depth += 1

        return depth


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
#     root = create_binary_tree([3, 9, 20, None, None, 15, 7])
#     result = solution.maxDepth(root)
#     print(result)  # Output: 3
