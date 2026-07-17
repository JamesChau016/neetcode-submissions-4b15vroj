class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        res=True
        d={}
        visited=set()

        for i in edges:
            if not d.get(i[0]):
                d[i[0]]=[i[1]]
            else:
                d[i[0]].append(i[1])
            if not d.get(i[1]):
                d[i[1]]=[i[0]]
            else:
                d[i[1]].append(i[0])

        def dfs(node,parent):
            nonlocal res
            if node in visited:
                res=False
                return
            
            visited.add(node)
            for i in d.get(node,[]):
                if i==parent:
                    continue
                dfs(i,node)

        dfs(0,-1)
        if len(visited)!=n:
            res=False
        
        return res
            