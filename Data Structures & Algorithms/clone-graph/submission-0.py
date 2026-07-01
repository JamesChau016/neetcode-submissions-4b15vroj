"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visited=set()
        hashMap={}
        def dfs(currNode):
            if not currNode:
                return
            if currNode in visited:
                return
            
            cloneNode=Node(currNode.val)
            hashMap[currNode]=cloneNode
            visited.add(currNode)

            for i in currNode.neighbors:
                dfs(i)
                cloneNode.neighbors.append(hashMap.get(i))
        
        currNode=node
        dfs(currNode)

        return hashMap[node]

