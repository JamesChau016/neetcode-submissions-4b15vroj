class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        suf=[]
        pre=[]
        n=len(height)
        for i in range(n):
            pre.append(max(height[0:i+1]))

        for i in range(n-1, -1, -1):
            suf.insert(0,max(height[i:n]))
        
        for i in range(n):
            ans+=min(pre[i],suf[i])-height[i]

        return ans
