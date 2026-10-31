from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        res = [] 
        
        dq = deque() # call the deque 

        for i in range(len(nums)):

            while dq and  dq[0] <= i-k :
                dq.popleft() 
            
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()  
            
            dq.append(i)
            
            if dq and i >= k-1 :
                res.append(nums[dq[0]]) 
        
        return res



        

        