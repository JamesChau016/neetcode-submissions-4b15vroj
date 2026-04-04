class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        freq={}
        for i in nums:
            freq[i]=0
        for i in nums:
            freq[i]+=1
        sort= sorted(freq.items(), key=lambda item: item[1],reverse=True)
        for i in range(k):
            ans.append(sort[i][0])

        return ans