class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+','-','*','/'}
        stack=[]

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                num2=stack.pop()
                num1=stack.pop()
                match i:
                    case '+':
                        res=num1+num2
                    case '-':
                        res=num1-num2
                    case '*':
                        res=num1*num2
                    case '/':
                        res=int(num1/num2)
                stack.append(res)
        
        return stack[0]