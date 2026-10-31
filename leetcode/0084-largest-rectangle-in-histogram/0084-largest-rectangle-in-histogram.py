class Solution(object):
    def largestRectangleArea(self, heights):
        # in finding PSE if smaller element not has found which means the stack empty it should return -1 

        # in finding NSE if smaller element not has found which means the stack empty it should return n 

        # area = heights[i] * ((nse[i] - pse[i]) -1)

        def nextSmallerElement(heights):
            stack = []
            res  = [n] * len(heights)  

            for i in range(len(heights)-1,-1,-1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack :
                    res[i] = stack[-1] #peek 
                else :
                    res[i] = n
                stack.append(i) 

            return res
        
        def previousSmallerElement(heights):
            stack = []
            res  = [-1] * len(heights)  

            for i in range(len(heights)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack :
                    res[i] = stack[-1] #peek 
                else :
                    res[i] = -1
                stack.append(i) 
            
            return res


            
        
        n = len(heights)

        NSE = nextSmallerElement(heights) 
        PSE = previousSmallerElement(heights) 
        max_area = 0
        
        for i in range(n):

            width = (NSE[i] - PSE[i]) -1
            area = heights[i] * width 
            max_area = max(max_area,area) 
        
        return max_area




