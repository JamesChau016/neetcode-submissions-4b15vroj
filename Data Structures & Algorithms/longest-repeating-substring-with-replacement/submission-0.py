class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq={}
        ans=0
        maxf=0
        l=0
        for i in range(len(s)):
            if not frq.get(s[i]):
                frq[s[i]]=1
            else:
                frq[s[i]]+=1
            if frq.get(s[i])>maxf:
                maxf=frq.get(s[i])
            
            length=i-l+1
            if length-maxf>k:
                frq[s[l]]-=1
                l+=1
            else:
                ans=max(length,ans)
        


        return ans