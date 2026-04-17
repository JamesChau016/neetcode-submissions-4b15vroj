class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[0]

        for i in range(1,n):
            
            if temperatures[i]>temperatures[i-1]:
                while len(stack)>0:
                    if temperatures[stack[-1]]>=temperatures[i]:
                        break
                    rm=stack.pop()
                    s= i-rm
                    print(rm)
                    ans[rm]+=s
                stack.append(i)
            else:
                stack.append(i)
        
        return ans
            