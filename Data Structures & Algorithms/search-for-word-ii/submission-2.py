class Node:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.index=-1

class PrefixTree:
    def __init__(self):
        self.head=Node()

    def insert(self, word: str, index: int) -> None:
        curr=self.head
        for i in word:
            if i in curr.children:
                curr=curr.children[i]
            else:
                curr.children[i]=Node()
                curr=curr.children[i]
        
        curr.isEnd=True
        curr.index=index


    def search(self, node, word: str):
        if word not in node.children:
            return None
        node=node.children[word]
        
        return node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=PrefixTree()
        for i in range(len(words)):
            trie.insert(words[i],i)

        res=[]
        visited=set()
        def backtrack(node,row,col):
            if node.index!=-1 and node.isEnd==True:
                res.append(words[node.index])
                node.index=-1
            
            if (row<0 or row>=len(board)) or (col<0 or col>=len(board[0])):
                return
            
            if (row,col) in visited:
                return
            
            word=board[row][col]
            node=trie.search(node,word)
            if node==None:
                return
        
            visited.add((row,col))
            backtrack(node,row+1,col)
            backtrack(node,row,col+1)
            backtrack(node,row-1,col)
            backtrack(node,row,col-1)
            visited.remove((row,col))
        
        node=trie.head
        for r in range(len(board)):
            for c in range(len(board[0])):
                if trie.search(node,board[r][c])==None:
                    continue
                backtrack(node,r,c)

        return res


        