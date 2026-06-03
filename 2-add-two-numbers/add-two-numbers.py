# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr1, curr2 = None, l1, l2
        tens = 0

        while curr1 and curr2:
            node_sum = curr1.val + curr2.val + tens
            tens = node_sum // 10
            ones = node_sum % 10
            curr1.val = ones
            prev = curr1
            curr1, curr2 = curr1.next, curr2.next

        if curr2:
            prev.next = curr2
            curr1 = curr2

        while curr1:
            node_sum = curr1.val + tens
            curr1.val = node_sum % 10
            tens = node_sum // 10
            print(tens)

            prev = curr1
            curr1 = curr1.next

        if tens > 0:
            prev.next = ListNode(tens)
            
        return l1