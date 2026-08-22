# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(node, max_, min_):
            if not node:
                return True
            
            left = dfs(node.left, node.val, min_)
            right = dfs(node.right, max_, node.val)

            return (min_ < node.val < max_) and left and right

        left = dfs(root.left, root.val, float('-inf'))
        right = dfs(root.right, float('inf'), root.val)
        
        return left and right