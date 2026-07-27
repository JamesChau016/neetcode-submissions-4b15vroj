class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:
            return s

        res=''
        def dp(l,r):
            nonlocal res
            if l<0 or r>=n:
                return 
            if s[l]!=s[r]:
                return
            
            res=s[l:r+1] if r+1-l>len(res) else res
            dp(l-1,r+1)
        
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp(i,i+1)
            
            dp(i,i)

        return res