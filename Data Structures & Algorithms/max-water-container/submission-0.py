class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=[]
        n=len(heights)
        l=0
        r=n-1
        while l<r:
            m=min(heights[l],heights[r])
            ans.append((r-l)*m)
            if m==heights[l]:
                l+=1
            else:
                r-=1
        return max(ans)
