class Solution(object):
    def sortColors(self, nums):
        low = 0 
        mid = 0 
        high = len(nums) - 1
        def swap(nums,mid,high):
            nums[mid],nums[high] = nums[high],nums[mid]

        while mid <= high :
            if nums[mid] == 2 :
                swap(nums,mid,high)
                high -= 1 
            elif nums[mid] == 0 :
                swap(nums,mid,low)
                mid += 1
                low += 1
            else :
                mid += 1 
        return nums
        