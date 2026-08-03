class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if triplets[0]==target:
            return True
        
        valids=[]
        for i in range(len(triplets)):
            for j in range(len(target)):
                valid=True
                if triplets[i][j]>target[j]:
                    valid=False
                    break
            if valid:
                valids.append(triplets[i])
        
        for i in range(len(valids)):
            for j in range(len(target)):
                if valids[i][j]==target[j]:
                    triplets[0][j]=valids[i][j]

        return triplets[0]==target                