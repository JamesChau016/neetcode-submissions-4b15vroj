class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges={}
        res=[]

        for i in tickets:
            if not edges.get(i[0]):
                edges[i[0]]=[i[1]]
            else:
                edges[i[0]].append(i[1])
        
        for key in edges:
            edges[key].sort(reverse=True)
        
        def dfs(node):
            nonlocal res

            while edges.get(node):
                val=edges.get(node).pop()
                dfs(val)

            res.append(node)

        dfs('JFK')

        return res[::-1]