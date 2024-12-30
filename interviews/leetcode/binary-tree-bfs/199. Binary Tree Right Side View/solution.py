# Define the TreeNode class to structure the binary tree nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the root is None, return an empty list
        if not root:
            return []

        # Initialize the result list to store the right side view
        result = []
        # Initialize a queue for BFS
        queue = [root]

        while queue:
            # Get the number of nodes at the current level
            level_length = len(queue)

            # Traverse all the nodes at this level
            for i in range(level_length):
                node = queue.pop(0)  # Dequeue a node

                # If this is the rightmost node at this level, add it to the result
                if i == level_length - 1:
                    result.append(node.val)

                # Enqueue the left and right children of the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# Uncomment to test the function
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.right = TreeNode(5)
#     root.right.right = TreeNode(4)
#     solution = Solution()
#     print(solution.rightSideView(root))  # Expected Output: [1, 3, 4]
