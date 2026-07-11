class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d={}
        seen=set()
        res=[]

        for i in prerequisites:
            if not d.get(i[0]):
                d[i[0]]=[i[1]]
            else:
                d[i[0]].append(i[1])
        
        def dfs(course,visited):
            nonlocal res,seen
            if course in visited:
                return False
            if course in seen:
                return True
            
            visited.add(course)
            
            for i in d.get(course,[]):
                if not dfs(i,visited):
                    return False
                    
            seen.add(course)
            res.append(course)
            d[course]=[]
            visited.remove(course)
            return True

        
        for i in range(numCourses):
            if not dfs(i,set()):
                return []
            
        return res
