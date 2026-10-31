class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)# edge case k > len(nums)
        
        def reverse(nums,start,end):
            while start <= end :
                nums[start],nums[end] = nums[end],nums[start] 
                start += 1 
                end -= 1  
        
        reverse(nums,0,len(nums)-1) # reverse whole arr 
        reverse(nums,0,k-1) # reverse first part till k-1
        reverse(nums,k,len(nums)-1) # reverse from k to len(arr)
        
        return nums
            
        

 
        
        
        
        