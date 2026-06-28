"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_nodes = []
        if not root:
            return None
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr_node = queue.popleft()
                if i < level_size - 1:
                    curr_node.next = queue[0]
                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

        return root