class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited=[-1]*len(cost)

        def dfs(index):
            if index>=len(cost):
                return 0
            if visited[index]!=-1:
                return visited[index]
            s=cost[index] + min(dfs(index+1),dfs(index+2))
            visited[index]=s
            return s

        return min(dfs(0),dfs(1))