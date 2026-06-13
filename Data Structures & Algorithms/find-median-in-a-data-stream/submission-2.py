import heapq
class MedianFinder:

    def __init__(self):
        self.upper=[]
        self.lower=[]
        heapq.heapify(self.upper)
        heapq.heapify(self.lower)

    def addNum(self, num: int) -> None:
        u=len(self.upper)
        l=len(self.lower)
        if l==0:
            heapq.heappush(self.lower, -num)
            return
        if u==0:
            heapq.heappush(self.upper, num)
            return
        
        if u==l==1 and self.upper[0]<-self.lower[0]:
            tmp1=heapq.heappop(self.upper)
            tmp2=heapq.heappop(self.lower)
            heapq.heappush(self.lower,-tmp1)
            heapq.heappush(self.upper,-tmp2)

        
        if num>self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        u=len(self.upper)
        l=len(self.lower)
        if u>l+1:
            x=-heapq.heappop(self.upper)
            heapq.heappush(self.lower,x)
        elif l>u+1:
            x=-heapq.heappop(self.lower)
            heapq.heappush(self.upper,x)

        

    def findMedian(self) -> float:
        u=len(self.upper)
        l=len(self.lower)


        if u*l==0:
            return self.upper[0] if l==0 else -self.lower[0]
        elif (u+l) % 2==0:
            res=(self.upper[0]-self.lower[0])/2
            return res
        else:
            return self.upper[0] if u>l else -self.lower[0]
        