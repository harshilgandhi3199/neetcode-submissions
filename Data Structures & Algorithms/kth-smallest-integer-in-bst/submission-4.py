# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative DFS (In-order) - use explicit stack
class Solution:
    # Avg case: Time - O(h + k) | Space - O(h)
    # Worst case: Time - O(n) | Space - O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right        