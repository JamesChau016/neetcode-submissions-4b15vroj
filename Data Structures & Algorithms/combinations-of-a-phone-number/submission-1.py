class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        d={'2':('a','b','c'),
            '3':('d','e','f'),
            '4':('g','h','i'),
            '5':('j','k','l'),
            '6':('m','n','o'),
            '7':('p','q','r','s'),
            '8':('t','u','v'),
            '9':('w','x','y','z')}

        def backtrack(s,index):
            if len(digits)==index:
                if s!='':
                    res.append(s)
                return

            n=len(d[digits[index]])
            for j in range(n):
                s+=d[digits[index]][j]
                backtrack(s,index+1)
                s=s[:-1]

        s=''
        index=0
        backtrack(s,index)
        return res