class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1

        while left < right :
            mid = left + (right-left)// 2 

            if nums[mid] < nums[mid+1] :
                left = mid + 1 
            else :
                right  = mid  
    
        return left







        # peakNum = nums[0]
        # index = 0
        # for i in range(1,len(nums)):
        #     if nums[i] > peakNum :
        #         peakNum = nums[i]
        #         index = i 
        
        # return index
        