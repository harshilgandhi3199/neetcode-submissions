# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#             4
#     2               5
# -1      3                6

# k=3
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        result = 0
        # in-order traversal
        node = root
        def dfs(node):
            nonlocal count, result
            if not node:
                return False

            if dfs(node.left):
                return True

            if count == k:
                result = node.val
                return True
            count += 1

            return dfs(node.right)

        dfs(root)
        return result