class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans=0
        heights.append(0)
        n=len(heights)

        stack=[]
        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            
            if heights[i]>=heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i]<heights[stack[-1]]:
                    h=heights[stack.pop()]
                    l=stack[-1] if stack else -1
                    area=h*(i-l-1)
                    ans=max(area,ans)
                stack.append(i)
        

        return ans