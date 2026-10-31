class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for ch in tokens:
            if ch == "-" :
                num1 = (stack.pop()) 
                num2 = (stack.pop())
                stack.append(num2-num1) 

            elif ch == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                result = abs(num2) / abs(num1)

                if (num1>0) != (num2>0): # check two numbers have opp sign to give neg sign to result
                    result = - result 
                    
                stack.append(result)

            
            elif ch == "+" :
                num1 = (stack.pop()) 
                num2 = (stack.pop())
                stack.append(num1 + num2)
            
            elif ch == "*":
                num1 = (stack.pop()) 
                num2 = (stack.pop())
                stack.append(num1 * num2)

            else :
                stack.append(int(ch))

        return stack.pop()

        
        