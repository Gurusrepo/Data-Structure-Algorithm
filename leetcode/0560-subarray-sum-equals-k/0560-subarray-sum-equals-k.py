class Solution(object):
    def subarraySum(self, nums, k):
        # sum - (sum - k) = k 
        count = 0
        p_sum = 0 
        sum_freq = {0:1}

        for num in nums :
            p_sum += num
            diff = p_sum - k

            if diff in sum_freq :
                count += sum_freq[diff] 
            sum_freq[p_sum] = sum_freq.get(p_sum,0) + 1  

        return count

        # brute force limit exceeded

        # count = 0

        # for i in range(len(nums)):
        #     crr = 0
        #     for j in range(i,len(nums)):
        #         crr += nums[j] 

        #         if crr == k :
        #             count += 1
        
        # return count



                

        
                 
        
            


    
 

            
        