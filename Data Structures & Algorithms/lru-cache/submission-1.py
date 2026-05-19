class ListNode:
    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.length=0
        self.hashMap={}
        self.left=ListNode(-1, -1)
        self.right=ListNode(-1, -1)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self, node) -> None:
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def append(self, node) -> None:
        prevNode=self.right.prev

        node.next=self.right
        self.right.prev=node
        prevNode.next=node
        node.prev=prevNode
        

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        node=self.hashMap.get(key)
        self.remove(node)
        self.append(node)
        
        return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap:
            node=ListNode(key, value)
            self.append(node)
            self.length+=1
        else:
            node=self.hashMap.get(key)
            node.val=value
            self.remove(node)
            self.append(node)

        self.hashMap[key]=node
        
        if self.length>self.cap:
            self.hashMap.pop(self.left.next.key)
            self.remove(self.left.next)
            
            self.length-=1


