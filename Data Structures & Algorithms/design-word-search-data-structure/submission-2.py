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
        def reSearch(word, curr) -> bool:
            if not word:
                if curr.isEnd==True:
                    return True
            elif word[0] in curr.children:
                return reSearch(word[1:], curr.children[word[0]])
            elif word[0]=='.':
                for j in curr.children:
                    if reSearch(word[1:], curr.children[j]):
                        return True
                else:
                    return False
            
            return False

        curr=self.head
        return reSearch(word,curr)
