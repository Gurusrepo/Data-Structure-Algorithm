class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        new_arr = []

        for i in range(n-2):

            if i == 0 or nums[i] != nums[i-1] :
                target = -nums[i]  
                left = i+1
                right = n-1 
                while left < right : 
                    currentElement = nums[left] + nums[right] 
                    if currentElement == target :

                        new_arr.append([nums[i],nums[left],nums[right]]) 

                        while left < right and nums[left] == nums[left+1] :
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        left += 1
                        right -= 1
                    
                    elif currentElement > target :
                        right -= 1 
                    
                    else :
                        left += 1
        
        return new_arr


