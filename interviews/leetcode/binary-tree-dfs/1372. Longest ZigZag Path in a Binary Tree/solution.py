
# Enum value for left and right directions
LEFT = 0
RIGHT = 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0  # To store the longest ZigZag path found

        # DFS function to explore the tree
        def dfs(node, direction, length):
            if not node:
                return

            # Update the max_length
            self.max_length = max(self.max_length, length)

            # If the direction is 0 (left), next move should be to the right
            if direction == LEFT:
                # Move right
                dfs(node.right, RIGHT, length + 1)  # Right move, increase length
                # Start a new ZigZag from left
                dfs(node.left, LEFT, 1)  # Start left direction with length 1
            else:
                # Move left
                dfs(node.left, LEFT, length + 1)  # Left move, increase length
                # Start a new ZigZag from right
                dfs(node.right, RIGHT, 1)  # Start right direction with length 1

        # Start the DFS from root, with two directions, left (0) and right (1)
        dfs(root, 0, 0)  # Start going left
        dfs(root, 1, 0)  # Start going right

        return self.max_length
