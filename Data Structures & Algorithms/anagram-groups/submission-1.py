class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]

        ans=[]
        d={}
        for i in strs:
            freq= [0]*26
            for j in i:
                freq[ord(j)-ord('a')]+=1
            d.setdefault(tuple(freq),[]).append(i)
        
        for i in d.values():
            ans.append(i)

        return ans