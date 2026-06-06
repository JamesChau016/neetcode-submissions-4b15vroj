# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        code=[]

        def dfs(root):
            nonlocal code
            if not root:
                code.append('N,')
                return
            
            code.append(f"{str(root.val)},")

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res=''.join(code)
        print(res)
        return res
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        index=0
        data=data.split(',')

        def dfs(n):
            nonlocal index
            if index>=n:
                return
            if data[index]=='N':
                return None
            
            root=TreeNode(int(data[index]))
            index+=1
            root.left=dfs(n)

            index+=1
            root.right=dfs(n)

            return root
        

        root=dfs(len(data))
        return root

