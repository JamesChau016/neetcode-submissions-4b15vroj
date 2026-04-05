class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=''.join(s.lower().split(' '))
        l=0
        r=len(s2)-1
    
        
        while l<r:
            if not s2[l].isalnum():
                l+=1
                continue
            if not s2[r].isalnum():
                r-=1
                continue
            if s2[l]!=s2[r]:
                return False
            l+=1
            r-=1

        return True