class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if triplets[0]==target:
            return True
        
        valids=triplets.copy()
        for i in range(1,len(triplets)):
            for j in range(len(target)):
                if triplets[i][j]>target[j]:
                    valids.remove(triplets[i])
                    break
        
        for i in range(len(valids)):
            for j in range(len(target)):
                if valids[i][j]==target[j]:
                    triplets[0][j]=valids[i][j]

        return triplets[0]==target                