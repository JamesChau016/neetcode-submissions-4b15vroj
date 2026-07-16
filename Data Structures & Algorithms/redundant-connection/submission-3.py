class UnionFind:
    def __init__(self):
        self.hashMap={}
    
    def find(self,node):
        if node not in self.hashMap:
            return node
        self.hashMap[node]=self.find(self.hashMap.get(node,None))  
        return self.hashMap[node]
    
    def union(self,u,v):
        parU=self.find(u)
        parV=self.find(v)
        if parU==parV:
            return False
        self.hashMap[parV]=parU
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d=UnionFind()

        for u,v in edges:
            if d.union(u,v):
                continue
            else:
                return [u,v]
        
        return []