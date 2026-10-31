class Solution:
    def isValid(self, s: str) -> bool: 

        # first off all i will appending the opp of open parantheses to stack until close come 
        # if the close come if will 
        # pop the stack check it matches with that close one 
        # true when not false in further iteration and until stack gets empty 
        # false return False 

        stack = [] 

        for i in s :
            if i == "(" :
                stack.append(")")
            elif i == "[" :
                stack.append("]")
            elif i == "{" :
                stack.append("}")  
            else :
                if not stack or stack.pop() != i :
                    return False 
        
        return not stack

        
        
        

              
                
                
        
        

        