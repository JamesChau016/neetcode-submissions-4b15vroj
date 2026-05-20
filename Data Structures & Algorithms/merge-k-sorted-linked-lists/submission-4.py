# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1: Optional[ListNode], l2: Optional[ListNode]):
            curr1=l1
            curr2=l2
            res= ListNode()
            temp= res

            
            while curr1 and curr2:
                if curr1.val<curr2.val:
                    temp.next=curr1
                    curr1=curr1.next
                else:
                    temp.next=curr2
                    curr2=curr2.next
                temp=temp.next
            
            if curr2:
                temp.next=curr2
            if curr1:
                temp.next=curr1
            
            return res.next
            
                
        n=len(lists)
        if n==0:
            return None
        elif n==1:
            return lists[0]
        
        inter=1
        while inter<n:
            for i in range(0,n,inter*2):
                if i+inter<n:
                    lists[i]=mergeList(lists[i],lists[i+inter])
                
            inter*=2
            
        
        return lists[0]
        
