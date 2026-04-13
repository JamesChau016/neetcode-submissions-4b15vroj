class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=''
        mlen=len(s)
        
        ds={}
        dt={}
        for i in t:
            if dt.get(i):
                dt[i]+=1
            else:
                dt[i]=1
            
        req=len(dt)
        formed=0
        l=0
        for r in range(len(s)):
            if ds.get(s[r]):
                ds[s[r]]+=1
            else:
                ds[s[r]]=1
            
            if dt.get(s[r]):
                if dt[s[r]]==ds[s[r]]:
                    formed+=1

            while formed==req:
                if r-l+1<=mlen:
                    mlen=r-l+1
                    ans=s[l:r+1]
                ds[s[l]]-=1
                if dt.get(s[l]):
                    if dt[s[l]]>ds[s[l]]:
                        formed-=1
                l+=1

        return ans