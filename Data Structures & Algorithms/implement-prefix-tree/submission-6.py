class Node:
    def __init__(self):
        self.children={}
        self.isEnd=False

class PrefixTree:
    def __init__(self):
        self.head=Node()

    def insert(self, word: str) -> None:
        curr=self.head
        for i in word:
            if i in curr.children:
                curr=curr.children[i]
            else:
                curr.children[i]=Node()
                curr=curr.children[i]
        
        curr.isEnd=True


    def search(self, word: str) -> bool:
        curr=self.head
        
        for i in word:
            if i not in curr.children:
                return False
            curr=curr.children[i]
        
        if curr.isEnd==False:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        curr=self.head
        
        for i in prefix:
            if i not in curr.children:
                return False
            curr=curr.children[i]
        
        return True
        