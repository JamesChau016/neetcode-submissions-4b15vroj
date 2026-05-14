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
        fast=head.next

        while fast:
            slow=slow.next
            try:
                fast=fast.next.next
            except AttributeError:
                break
        
        curr=slow
        prev=None
        nextNode=curr

        while curr:
            nextNode=nextNode.next
            curr.next=prev
            prev=curr
            curr=nextNode
        
        curr2=head

        while curr2.next!=slow:
            curr2=curr2.next
        
        curr2.next=None
        
        i=prev
        j=head
        tempi=i
        tempj=j
        while i:
            if tempj:
                tempj=tempj.next
                j.next=i
                j=tempj
            
            tempi=tempi.next
            if j:
                i.next=j
            else:
                i.next=tempi
            i=tempi

        
        


