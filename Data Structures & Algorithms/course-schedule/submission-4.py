class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d={}
        res=True

        for i in prerequisites:
            if not d.get(i[0]):
                d[i[0]]=[i[1]]
            else:
                d[i[0]].append(i[1])

        def dfs(course,visited):
            nonlocal res
            if not d.get(course):
                return

            visited.add(course)
            for i in d.get(course):
                if i in visited:
                    res=False
                    return
                dfs(i,visited)
            visited.remove(course)
        
        for i in range(numCourses):
            dfs(i,set())

        return res

