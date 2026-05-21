# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            curr=head
            prev=None
            while curr:
                nextNode=curr.next
                curr.next=prev
                prev=curr
                curr=nextNode
            
            return (prev,head)
        
        if not head:
            return None
        

        dummy=ListNode(-1)
        curr=head
        prev=None
        prevTail=None
        while curr:
            tempHead=curr
            n=0
            for i in range(k):
                if not curr:
                    break
                
                n+=1
                prev=curr
                curr=curr.next
            
            if n==k:
                prev.next=None
                newHead,tail=reverse(tempHead)
                if prevTail==None:
                    dummy.next=newHead
                else:
                    prevTail.next=newHead
                prevTail=tail
            else:
                prevTail.next=tempHead
            
        return dummy.next