# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getDepth(root,l,r):
            if not root:
                return 0
            

            if root.left:
                l+=1
            if root.right:
                r+=1
            
            return 1+max(getDepth(root.left,l,r),getDepth(root.right,l,r))
        l=0
        r=0
        return getDepth(root,l,r)