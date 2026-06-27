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
        def reSearch(index, curr) -> bool:
            for i in range(index, len(word)):
                if word[i]=='.':
                    for j in curr.children:
                        newCurr=curr.children[j]
                        if reSearch(i+1, newCurr):
                            return True
                    else:
                        return False
                
                if word[i] not in curr.children:
                    return False

                curr=curr.children[word[i]]

            if curr.isEnd==False:
                return False
            
            return True    

        curr=self.head
        index=0
        return reSearch(index,curr)
