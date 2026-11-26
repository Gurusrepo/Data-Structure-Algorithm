class Solution(object):
    def generateParenthesis(self, n):
        arr = [] 


        def generate(openCount,closeCount,pair):

            if len(pair) == n * 2 :
                arr.append(pair) 
                return
            
            if openCount < n :
                generate(openCount+1,closeCount,pair+"(") 

            if closeCount < openCount : 
                generate(openCount, closeCount+1, pair+")")

        generate(0,0,"")

        return arr
        