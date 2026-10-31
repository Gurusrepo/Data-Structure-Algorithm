class Solution(object):
    def find132pattern(self, nums):
        stack = [] # PGE & min_value 
        min_value = nums[0] 

        for n in nums[1:]:
            while stack and n >= stack[-1][0] : # means reverse of [0] (last element)
                stack.pop()
            if stack and stack[-1][1] < n and stack[-1][0] > n :  # means reverse[0] 
                return True

            min_value = min(n,min_value) 
            stack.append([n,min_value]) 

        return False
