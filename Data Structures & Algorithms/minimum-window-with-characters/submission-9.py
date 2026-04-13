class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(ds: Dict, dt: Dict) -> bool:
            for k,v in dt.items():
                if ds.get(k):
                    if ds.get(k) < v:
                        return False
                else:
                    return False
            return True
        
        ans=''
        mlen=len(s)
        # if len(s)==1:
        #     return s if s==t else ''
        
        ds={}
        dt={}
        for i in t:
            if dt.get(i):
                dt[i]+=1
            else:
                dt[i]=1
        
        l=0
        for r in range(len(s)):
            if ds.get(s[r]):
                ds[s[r]]+=1
            else:
                ds[s[r]]=1
            
            while check(ds,dt):
                if r-l+1<=mlen:
                    mlen=r-l+1
                    ans=s[l:r+1]
                ds[s[l]]-=1
                l+=1


        return ans