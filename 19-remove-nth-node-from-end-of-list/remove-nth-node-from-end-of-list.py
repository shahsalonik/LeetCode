# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        curr = head
        target_ind = size - n
        curr_ind = 0

        if target_ind == 0:
            return head.next

        while curr:
            if curr_ind + 1 == target_ind:
                curr.next = curr.next.next
                break
            curr = curr.next
            curr_ind += 1

        return head