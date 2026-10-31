class Solution(object):
    def sortedSquares(self, nums):

        left = 0 
        right = len(nums)-1 
        new_arr = [0] * len(nums)

        for i in range(-1,-(len(nums)+1),-1):

            if abs(nums[left]) > abs(nums[right]):
                new_arr[i] = nums[left] ** 2
                left +=1 
            else :
                new_arr[i] = nums[right] ** 2
                right -= 1
            
        return new_arr



        # for i in range(len(nums)) :
        #     nums[i] = nums[i] ** 2          # o(n log n)
        
        # nums.sort()
        # return nums

       