class Solution:
   def partitionLabels(self, s: str) -> List[int]:
        hashMap={}
        for i in range(len(s)):
            hashMap[s[i]]=i
        
        res=[]
        end=0
        start=-1
        for i in range(len(s)):
            end=max(hashMap[s[i]],end)
            if i==end:
                res.append(end-start)
                start=i

        return res