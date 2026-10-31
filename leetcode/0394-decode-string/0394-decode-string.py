class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s :

            if i != "]":
                stack.append(i)
            else :
                temp = ""
                while stack[-1] != "[" :
                    temp = stack.pop() + temp 
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit() :
                    num = str(stack.pop()) + num 
                
                stack.append(temp * int(num))
            
        return "".join(stack)





        return "".join(stack)

                  
            
