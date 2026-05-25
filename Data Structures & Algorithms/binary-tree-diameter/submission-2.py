# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        maxD=0

        def getDepth(root):
            nonlocal maxD
            if not root:
                return 0
            
            l=getDepth(root.left)
            r=getDepth(root.right)

            maxD=max(maxD, l+r)
            
            return 1+max(l,r)
        
        getDepth(root)
        return maxD
        

    
    