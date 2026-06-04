# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum=root.val

        def dfs(root):
            nonlocal maximum
            if not root:
                return 0
            
            lsum=max(0,dfs(root.left))
            rsum=max(0,dfs(root.right))
            sum=root.val+lsum+rsum

            maximum=max(sum,maximum)

            return root.val+max(lsum,rsum)
        
        dfs(root)
        return maximum