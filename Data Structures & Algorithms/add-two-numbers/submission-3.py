# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        res=ListNode()

        c1=l1
        c2=l2
        c3=res
        carry=0
        while c1 and c2:
            s=c1.val+c2.val+carry
            c3.next=ListNode(s%10)
            carry=s//10
            c1=c1.next
            c2=c2.next
            c3=c3.next
        
        while c1:
            s=c1.val+carry
            c3.next=ListNode(s%10)
            carry=s//10
            c1=c1.next
            c3=c3.next

        while c2:
            s=c2.val+carry
            c3.next=ListNode(s%10)
            carry=s//10
            c2=c2.next
            c3=c3.next

        if carry!=0:
            c3.next=ListNode(carry)
        
        return res.next
