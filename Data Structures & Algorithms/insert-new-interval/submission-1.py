class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        mark=0
        n=len(intervals)
        for i in range(n):
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
                mark=i+1
        
        mark2=mark
        for i in range(mark,n):
            if intervals[i][1]>=newInterval[0] and intervals[i][0]<newInterval[1]:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                mark2=i+1
            if intervals[i][0]<=newInterval[1] and intervals[i][1]>newInterval[0]:
                newInterval[1]=max(intervals[i][1],newInterval[1])
                mark2=i+1
        
        res.append(newInterval)
        
        for i in range(mark2,n):
            res.append(intervals[i])

        return res