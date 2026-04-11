class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(', ']':'[', '}':'{'}
        seen=[]


        for i in s:
            if i in d.values():
                seen.append(i)
            else:
                if len(seen)!=0 and d.get(i)==seen[-1]:
                    seen.pop()
                else:
                    return False
        
        return len(seen)==0