class Solution(object):
    def majorityElement(self, nums):
        # count = {}
        # for num in nums:
        #     if num in count :
        #         count[num] = count[num] + 1 
        #     else :
        #         count[num] = 1
        # return max(count, key = count.get)
        
        count = 0
        curr = 0 
        for num in nums :
            if count == 0 :
                curr = num
            if num != curr :
                count -= 1
            else :
                count += 1
        
        return curr
        
    

        

        

        