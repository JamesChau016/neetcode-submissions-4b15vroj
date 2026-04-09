class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        m=0
        l=0
        
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                m=max(m, i-l+1)
            else:
                while s[l]!= s[i]:
                    seen.remove(s[l])
                    l+=1
                l+=1



        return m

