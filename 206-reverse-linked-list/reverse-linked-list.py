# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # store the next node
            temp = curr.next
            
            # update next pointer
            curr.next = prev 

            prev = curr
            curr = temp
        
        return prev