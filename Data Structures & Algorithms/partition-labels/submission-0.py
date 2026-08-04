from collections import defaultdict
class Solution:
   def partitionLabels(self, s: str) -> List[int]:
        hashMap=defaultdict(int)
        for i in range(len(s)):
            if hashMap[s[i]]<i:
                hashMap[s[i]]=i
        
        res=[]
        size=0
        start=-1
        for i in range(len(s)):
            size=max(hashMap[s[i]]-start,size)
            if i==(size+start):
                res.append(size)
                size=0
                start=i

        return res