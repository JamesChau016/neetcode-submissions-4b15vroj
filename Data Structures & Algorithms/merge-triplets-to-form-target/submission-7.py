class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if triplets[0]==target:
            return True
        
        track=[False]*len(target)
        for i in range(len(triplets)):
            valid=True
            for j in range(len(target)):
                if triplets[i][j]>target[j]:
                    valid=False
                    break
            if valid:
                for t in range(len(target)):
                    if triplets[i][t]==target[t]:
                        track[t]=True

            if all(track):
                return True

        return False            