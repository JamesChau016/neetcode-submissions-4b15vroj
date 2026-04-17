class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                rm=stack.pop()
                ans[rm]+=i-rm
            stack.append(i)

        return ans
            