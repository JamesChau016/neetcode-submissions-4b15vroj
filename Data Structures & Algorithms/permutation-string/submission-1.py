class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1={}
        freq2={}

        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            if freq1.get(s1[i]):
                freq1[s1[i]]+=1
            else:
                freq1[s1[i]]=1
            if freq2.get(s2[i]):
                freq2[s2[i]]+=1
            else:
                freq2[s2[i]]=1
        
        if freq1==freq2:
            return True
        
        l=0
        for i in range(len(s1),len(s2)):
            freq2[s2[l]]-=1
            if freq2[s2[l]]==0:
                freq2.pop(s2[l])

            l+=1
            if freq2.get(s2[i]):
                freq2[s2[i]]+=1
            else:
                freq2[s2[i]]=1
            
            if freq1==freq2:
                return True



        return False