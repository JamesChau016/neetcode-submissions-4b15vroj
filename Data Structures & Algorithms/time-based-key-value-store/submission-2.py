class TimeMap:

    def __init__(self):
        self.timeMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.timeMap.get(key):
            self.timeMap[key]=[(value, timestamp)]
        else:
            self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeMap.get(key):
            return ""
        
        vals= self.timeMap.get(key)
        n=len(vals)
        
        if n==1:
            return vals[0][0] if vals[0][1]<=timestamp else ""
        
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if vals[mid][1]>timestamp:
                r=mid-1
            elif vals[mid][1]<timestamp:
                l=mid+1
            else:
                return vals[mid][0]

        return vals[r][0] if vals[r][1]<timestamp else ""
