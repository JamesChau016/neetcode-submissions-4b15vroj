from collections import deque,defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        wordList.append(beginWord)
        hashMap=defaultdict(list)
        visited=set([beginWord])
        n=len(beginWord)
        
        for word in wordList:
            for i in range(n):
                w=list(word)
                w[i]='*'
                pat=''.join(w)
                hashMap[pat].append(word)
        
        print(hashMap)
        queue=deque([(beginWord,1)])
        while queue:
            word,count=queue.popleft()

            if word==endWord:
                return count
            
            for i in range(n):
                w=list(word)
                w[i]='*'
                pat=''.join(w)

                for j in hashMap[pat]:
                    if j not in visited:
                        visited.add(j)
                        queue.append((j,count+1))
            

        return 0

