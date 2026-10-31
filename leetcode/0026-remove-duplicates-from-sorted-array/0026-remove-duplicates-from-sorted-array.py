class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
               nums.remove(nums[right])
            else :
                left += 1
                right += 1
        
        return len(nums)


        
