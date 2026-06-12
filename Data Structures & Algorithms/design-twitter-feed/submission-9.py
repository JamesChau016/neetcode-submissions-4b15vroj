import heapq
class Twitter:

    def __init__(self):
        self.followMap={}
        self.tweetMap={}
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if self.tweetMap.get(userId)==None:
            self.tweetMap[userId]=[(self.count,tweetId)]
        else:
            self.tweetMap[userId].append((self.count,tweetId))
        
        if self.followMap.get(userId)==None:
            self.followMap[userId]={userId}

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap.get(userId).add(userId)
        feed=[]
        heapq.heapify(feed)
        for i in self.followMap.get(userId,[]):
            for j in self.tweetMap.get(i,[]):
                heapq.heappush(feed,j)
                if len(feed)>10:
                    heapq.heappop(feed)
        
        res=[]
        while feed:
            res.append(heapq.heappop(feed)[1])
        
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if self.followMap.get(followerId)==None:
            self.followMap[followerId]={followeeId}
        else:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId and followeeId in self.followMap.get(followerId,[]):
            self.followMap[followerId].remove(followeeId)
