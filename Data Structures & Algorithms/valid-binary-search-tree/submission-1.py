# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid=True
        def dfs(root,maximum,minimum):
            nonlocal isValid
            if not root:
                return
            
            if root.val<=minimum or root.val>=maximum:
                isValid=False
                return
            
            dfs(root.left,root.val,minimum)
            dfs(root.right,maximum,root.val)
            
        maximum=math.inf
        minimum=-math.inf
        dfs(root,maximum,minimum)
        return isValid
            
