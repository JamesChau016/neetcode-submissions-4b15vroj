class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[i for i in s]
        s2=[i for i in t]
        
        return sorted(s1)==sorted(s2)