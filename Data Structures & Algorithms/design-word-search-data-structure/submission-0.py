class Node:
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.head=Node()

    def addWord(self, word: str) -> None:
        curr=self.head

        for i in word:
            if i not in curr.children:
                curr.children[i]=Node()
                curr=curr.children[i]
            else:
                curr=curr.children[i]

        
        curr.isEnd=True

    def search(self, word: str) -> bool:
        curr=self.head

        for i in range(len(word)):
            if word[i]=='.':
                for j in curr.children:
                    newWord=word[:i]+j+word[i+1:]   
                    if self.search(newWord):
                        return True
                else:
                    return False
            
            if word[i] not in curr.children:
                return False

            curr=curr.children[word[i]]

        if curr.isEnd==False:
            return False
        
        return True    
