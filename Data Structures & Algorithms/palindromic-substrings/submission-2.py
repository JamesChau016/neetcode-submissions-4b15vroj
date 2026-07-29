class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        def dp(start,end):
            nonlocal res
            if end>=len(s) or start<0:
                return
            if s[start]!=s[end]:
                return
            res+=1
            dp(start-1,end+1)
        
        for i in range(len(s)):
            if i+1<len(s) and s[i]==s[i+1]:
                dp(i,i+1)
            dp(i,i)
        
        return res