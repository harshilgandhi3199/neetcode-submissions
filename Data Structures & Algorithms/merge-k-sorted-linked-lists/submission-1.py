# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Approach 1
        # unpack values of each linked list into an intermediate list
        # sort that list
        # create a new linked list from the sorted list

        # Approach 2
        # dump all the values into a min-heap as we traverse each
        # linked list
        # Pop from the min-heap into a single linked list

        # Approach 3
        # Add each list node to the min-heap
        # Pop the top list node as curr_node, save that node to the final linked list
        # Do curr_node.next, add it back to the heap is curr_node.next is not None
        # Keep doing above until heap is empty.
        min_heap = []
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, id(node), node))

        node = None
        merged_head = ListNode()
        while min_heap:
            _, _, curr_node = heapq.heappop(min_heap)
            if not merged_head.next:
                node = curr_node
                merged_head.next = node
                curr_node = curr_node.next
                node.next = None
            else:
                node.next = curr_node
                curr_node = curr_node.next
                node = node.next
            if curr_node:
                heapq.heappush(min_heap, (curr_node.val, id(curr_node), curr_node))

        return merged_head.next
            