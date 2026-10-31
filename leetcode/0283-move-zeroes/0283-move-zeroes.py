class Solution(object):
    def moveZeroes(self, nums):

        #right take care non zero element to place at the beggining and swap 0 to the place 
        #left will take care the pointer of zero in the curr index 

        left = 0 

        for right in range(len(nums)):

            if nums[right] != 0 :
                
                nums[left],nums[right] = nums[right],nums[left] 
                left += 1 

        return nums


        # left = 0 
        # right = 0

        # while left < len(nums) and right < len(nums):
        #     if nums[left] != 0 :
        #         left += 1
        #         right = left

        #     elif nums[left] == 0 and nums[right] == 0 :
        #         right += 1 
            
        #     else :
        #         nums[left],nums[right] = nums[right],nums[left]
        
        # return nums