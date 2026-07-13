class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res=0
        visited=set()
        d={}

        for i in edges:
            if not d.get(i[0]):
                d[i[0]]=[i[1]]
            else:
                d[i[0]].append(i[1])
            if not d.get(i[1]):
                d[i[1]]=[i[0]]
            else:
                d[i[1]].append(i[0])

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for i in d.get(node,[]):
                dfs(i)
        
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res+=1
        
        return res
