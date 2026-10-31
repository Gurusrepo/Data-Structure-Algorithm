class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        left = -1
        max_len = 0

        for i in range(len(s)) :

            if s[i] == "(" :
                stack.append(i) 
            else:
                if not stack :
                    left = i
                else :
                    stack.pop()
                    if not stack :
                        max_len = max(max_len, i-left)
                    else :
                        max_len = max(max_len, i- stack[-1]) 
        
        return max_len


        
        return count
   
    
        

                

        