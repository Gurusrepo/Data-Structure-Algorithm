class Solution(object):
    def productExceptSelf(self, nums):
        new_arr = [0] * len(nums)
        p_sum = [0] * len(nums)
        s_sum = [0] * len(nums)

        product_sum = 1

        for i in range(len(nums)):
            product_sum *= nums[i]
            p_sum[i] = product_sum
        

        product_sum = 1
        
        for i in range(-1, -(len(nums))-1 , -1):
            product_sum *= nums[i]
            s_sum[i] = product_sum
       
            
            
        new_arr[0] = s_sum[1]
        new_arr[len(nums)-1] = p_sum[len(nums)-2] 

        for i in range(1,len(nums)-1):
            new_arr[i] = p_sum[i-1] * s_sum[i+1]
        
        return new_arr

        



        