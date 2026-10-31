class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for i in range(-1,-(len(temperatures)+1),-1):
            while stack and temperatures[stack[-1]] <= temperatures[i] :
                stack.pop()
            if stack :
                res[i] = stack[-1] - len(temperatures)-i
            stack.append(len(temperatures)+i) 
        
        return res

