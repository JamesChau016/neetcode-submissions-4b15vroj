# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        count=0
        first=head
        while count<n:
            first=first.next
            count+=1
        
        second=None
        while first:
            if not second:
                second=head
            else:
                second=second.next
            first=first.next
        
        if second:
            second.next=second.next.next
        else:
            return head.next
        return head
        
        