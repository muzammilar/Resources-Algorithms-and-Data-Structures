class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Dictionary to keep track of prefix sums and their counts
        prefix_sum_count = {0: 1}  # Base case: 0 sum exists once (to account for paths starting from the root)
        return self.dfs(root, targetSum, 0, prefix_sum_count)

    def dfs(self, root: TreeNode, target: int, current_sum: int, prefix_sum_count: dict) -> int:
        if not root:
            return 0

        # Update the current running sum
        current_sum += root.val

        # Check if there's any previous sum such that current_sum - target is in the map
        result = prefix_sum_count.get(current_sum - target, 0)

        # Record the current sum in the map
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        # Recurse on the left and right children
        result += self.dfs(root.left, target, current_sum, prefix_sum_count)
        result += self.dfs(root.right, target, current_sum, prefix_sum_count)

        # Backtrack: remove the current sum from the map
        prefix_sum_count[current_sum] -= 1

        return result


# Main function is commented by default
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(11)
# solution = Solution()
# result = solution.pathSum(root, 8)
# print(result)  # Expected output: 3
# resultIterative = solution.pathSumIterative(root, 8)
# print(resultIterative)  # Expected output: 3
