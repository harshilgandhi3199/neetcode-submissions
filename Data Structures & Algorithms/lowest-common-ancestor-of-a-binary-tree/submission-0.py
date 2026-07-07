# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # post-order traversal
        def dfs(node):
            #base case - didn't find p or q
            if not node:
                return None

            # found either p or q
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            #if both left and right returned node
            if left and right:
                return node

            return left if left else right

        return dfs(root)
            