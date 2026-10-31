class Solution(object):
    def findMaxLength(self, nums):
        p_sum = 0
        longest = 0 
        psum_table = {}

        for i in range(len(nums)):
            if nums[i] == 0 :
                p_sum += -1 
            else :
                p_sum += 1 
            
            #second condition 
            if p_sum == 0 :
                longest = i +1
            elif p_sum in psum_table :
                longest = max(longest, i - psum_table[p_sum])
            else :
                psum_table[p_sum] = i
            
        return longest

