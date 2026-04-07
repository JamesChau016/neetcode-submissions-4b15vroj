class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        suf=[height[n-1]]
        pre=[height[0]]

        m1=pre[0]
        for i in range(1,n):
            if height[i]>m1:
                m1=height[i]
            pre.append(m1)

        m2=suf[0]
        for i in range(n-2, -1, -1):
            if height[i]>m2:
                m2=height[i]
            suf.insert(0,m2)
        
        for i in range(n):
            ans+=min(pre[i],suf[i])-height[i]

        return ans
