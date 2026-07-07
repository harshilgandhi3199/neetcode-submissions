# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 9 -> 9 -> 7 741 + 959 = 1700
        # 9 -> 9 -> 9
                    # l1
        # 8 -> 9 -> 7 -> 
        # 10 - 9 = 1 (carry)
        # carry + l1.val + l2.val = 10 % 10 = 1(carry)
        #                         curr.val = num - 10
        lenght_l1 = 0
        length_l2 = 0
        curr = l1
        while curr:
            lenght_l1 += 1
            curr = curr.next

        curr = l2
        while curr:
            length_l2 += 1
            curr = curr.next

        if length_l2 > lenght_l1:
            l1, l2 = l2, l1

        carry = 0
        node = l1
        while True:
            totalSum = node.val + carry
            if l2:
                totalSum += l2.val
                l2 = l2.next
            if totalSum > 9:
                node.val = totalSum % 10
                carry = totalSum // 10
            else:
                node.val = totalSum
                carry = 0
            if node.next:
                node = node.next
            else:
                break

        if carry > 0:
            newNode = ListNode(carry, None)
            node.next = newNode

        return l1