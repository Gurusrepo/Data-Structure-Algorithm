class Solution(object):
    def searchRange(self, nums, target):
        
        def Ocurrence(nums,target):
            left = 0 
            right = len(nums) 

            while left < right :
                mid = left + (right-left)//2 

                if nums[mid] < target :
                    left = mid + 1
                else :
                    right = mid 

            return left 
        
        firstOcurrence = Ocurrence(nums,target) 

        if firstOcurrence == len(nums) or nums[firstOcurrence] != target :
            return [-1,-1]
        
        return [firstOcurrence, Ocurrence(nums,target+1) -1 ]
         

        
            
        
        
