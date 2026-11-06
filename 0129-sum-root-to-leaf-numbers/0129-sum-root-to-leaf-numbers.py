# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:

        def sumAdder_dfs(node, sum_root):
            if node is None:
                return 0
            sum_root = sum_root * 10 + node.val
            if node.left is None and node.right is None:
                return sum_root
            left = sumAdder_dfs(node.left, sum_root)
            right = sumAdder_dfs(node.right, sum_root)

            return left + right

        return sumAdder_dfs(root, 0)
        