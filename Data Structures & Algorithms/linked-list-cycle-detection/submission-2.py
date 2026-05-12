# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next==None:
            return False
        
        slow=head
        fast=head.next

        while slow!=fast:
            slow=slow.next
            try:
                fast=fast.next.next
            except AttributeError:
                return False
        
        return True