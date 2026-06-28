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
    # curr_node = 4
    # next_node = 5
    # curr_node.next = next_node
    # level-order traversal
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_nodes = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev_node = queue[0]
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node == None:
                    break
                if prev_node != curr_node:
                    prev_node.next = curr_node
                    prev_node = curr_node    

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            # curr_node.next = null

        return root

        