# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        elif not head.next:
            return

        slow=head
        fast=head

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None
        
        curr=second
        prev=None
        nextNode=curr

        while curr:
            nextNode=nextNode.next
            curr.next=prev
            prev=curr
            curr=nextNode
        
        i=prev
        j=head
        tempi=i
        tempj=j
        while i:
            tempi=tempi.next
            tempj=tempj.next
            j.next=i
            i.next=tempj
            j=tempj
            i=tempi
