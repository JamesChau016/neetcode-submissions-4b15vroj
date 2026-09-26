class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1==text2:
            return len(text1)
        
        memo={}
        def dp(t1,t2):
            if (t1==len(text1)) or (t2==len(text2)):
                return 0
            
            if memo.get((t1,t2))!=None:
                return memo.get((t1,t2))
            
            common=0
            if (text1[t1]==text2[t2]):
                common+=1+dp(t1+1,t2+1)
                memo[(t1,t2)]=common
                return common
            else:
                longest=max(dp(t1+1,t2),dp(t1,t2+1))
                memo[(t1,t2)]=longest
                return longest

        dp(0,0)

        return max(memo.values()) if memo.values() else 0
