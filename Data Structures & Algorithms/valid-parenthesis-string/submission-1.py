class Solution:
    def checkValidString(self, s: str) -> bool:
        stars=[]
        left=[]

        for i in range(len(s)):
            if s[i]=='(':
                left.append(('(',i))
            elif s[i]=='*':
                stars.append(('*',i))
            else:
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while left:
            if not stars:
                return False
            if stars[-1][1]<left[-1][1]:
                return False
            left.pop()
            stars.pop()

        return True