"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        hashMap={}
        curr=head
        while curr:
            l=Node(curr.val)
            hashMap[curr]=l
            curr=curr.next

        curr=head
        l=hashMap[head]
        curr2=l
        while curr:
            curr2.next=hashMap.get(curr.next)
            curr2.random=hashMap.get(curr.random)
            curr2=curr2.next
            curr=curr.next
        
        return l