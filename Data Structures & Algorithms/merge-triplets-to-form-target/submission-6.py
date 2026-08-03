class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if triplets[0]==target:
            return True
        
        valids=[]
        track=[-1]*len(target)
        for i in range(len(triplets)):
            for j in range(len(target)):
                valid=True
                if triplets[i][j]>target[j]:
                    valid=False
                    break
            if valid:
                for t in range(len(target)):
                    if triplets[i][t]==target[t]:
                        track[t]=0

        return sum(track)==0               