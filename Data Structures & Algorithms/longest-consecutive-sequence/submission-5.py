class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni=set(nums)
        m=0
        for i in uni:
            if i-1 not in uni:
                curr=i
                count=1

                while curr+1 in uni:
                    curr=curr+1
                    count+=1
                m=max(count,m)
                
        return m