from collections import defaultdict
class UnionFind:
    def __init__(self,nodes):
        norm=[tuple(i) for i in nodes]
        self.parent={n: n for n in norm}
        self.rank={n: 0 for n in norm}
    
    def find(self,node):
        node=tuple(node)
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self,node1,node2):
        root1=self.find(tuple(node1))
        root2=self.find(tuple(node2))

        if root1!=root2:
            if self.rank[root1]>self.rank[root2]:
                self.parent[root2]=root1
            elif self.rank[root1]<self.rank[root2]:
                self.parent[root1]=root2
            else:
                self.parent[root2]=root1
                self.rank[root1]+=1
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res=0
        edges=[]
        dsu=UnionFind(points)

        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                s=abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append(((points[i],points[j]),s))

        sortedEdges=sorted(edges, key=lambda edge: edge[1])

        for node,cost in sortedEdges:
            u,v = node

            if dsu.union(u,v):
                res+=cost
        
        return res