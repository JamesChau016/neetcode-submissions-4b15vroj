# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame=True

        def getVal(r1,r2):
            nonlocal isSame
            if not r1 and not r2:
                return

            if not r1 or not r2:
                isSame=False
                return
                
            if r1.val!=r2.val:
                isSame=False
                return

            getVal(r1.left,r2.left)
            getVal(r1.right,r2.right)

        getVal(p,q)
        return isSame
