class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(subnet,index):
            if index==len(nums):
                res.append(subnet[:])
                return
            
            subnet.append(nums[index])

            backtrack(subnet, index+1)

            subnet.pop()
            
            backtrack(subnet,index+1)

        index=0
        subnet=[]
        backtrack(subnet,index)
        return res