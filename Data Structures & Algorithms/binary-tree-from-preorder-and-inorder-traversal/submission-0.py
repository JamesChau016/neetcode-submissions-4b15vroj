# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index=0
        
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i

        def dfs(l,r):
            nonlocal index
            if l>r:
                return
            
            val=preorder[index]
            root= TreeNode(val)
            index+=1

            root_id=d[val]

            root.left=dfs(l,root_id-1)
            root.right=dfs(root_id+1,r)
            return root
            
        
        root=dfs(0,len(inorder)-1)
        return root
        
            

            

            
            