# Define the TreeNode class to structure the binary tree nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # If the root is None, return 0 as there's no level
        if not root:
            return 0

        # Initialize a queue for level order traversal (BFS)
        queue = [root]
        max_sum = float('-inf')  # Start with a very small value
        level = 0  # To track the current level
        max_level = 0  # To track the level with the maximum sum

        # Perform level order traversal
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_sum = 0  # Sum of values at the current level
            level += 1  # Move to the next level

            # Traverse all nodes at the current level
            for _ in range(level_size):
                node = queue.pop(0)  # Dequeue a node
                current_sum += node.val  # Add node's value to the sum

                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # If the sum at the current level is greater than the max_sum, update max_sum and max_level
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level

        return max_level

# Uncomment to test the function
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.right = TreeNode(6)
#     solution = Solution()
#     print(solution.maxLevelSum(root))  # Expected Output: 3
