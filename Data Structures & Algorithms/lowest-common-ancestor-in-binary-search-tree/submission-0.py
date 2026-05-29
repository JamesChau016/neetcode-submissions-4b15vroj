# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res=TreeNode()
        def dfs(root):
            nonlocal res
            if not root:
                return
            
            if p.val<root.val<q.val or q.val<root.val<p.val:
                res=root
                return
            elif root.val==p.val or root.val==q.val:
                res=p if root.val==p.val else q
                return
            
            dfs(root.left)
            dfs(root.right)

        
        if not root:
            return None
        
        dfs(root)
        return res
