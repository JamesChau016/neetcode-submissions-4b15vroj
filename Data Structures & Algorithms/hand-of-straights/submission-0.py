from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False

        hand.sort()
        d=defaultdict(int)

        for i in hand:
            d[i]+=1

        for card in hand:
            if d[card]==0:
                continue
            start=card
            for i in range(groupSize):
                print(start+i,d[start+i])
                if d[start+i]==0:
                    return False
                
                d[start+i]-=1

        return True