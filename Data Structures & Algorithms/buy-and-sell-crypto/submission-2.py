class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        m=prices[0]
        ans=0
        for i in range(1,n):
            ans=max(ans,prices[i]-m)
            if prices[i]<m:
                m=prices[i]
            
        
        return ans