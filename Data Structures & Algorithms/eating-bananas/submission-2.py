class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc(rate: int):
            s=0
            for i in piles:
                s+=math.ceil(i/rate)
            return s
        maximum=max(piles)
        n=len(piles)

        if n==h:
            return maximum
        
        l=1
        r=maximum
        while l<=r:
            mid= (l+r)//2
            s=calc(mid)
            if s>h:
                l=mid+1
            else:
                r=mid-1
        
        return l