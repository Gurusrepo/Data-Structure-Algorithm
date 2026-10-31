class Solution(object):
    def containsDuplicate(self, nums):
        
        nums_set = set()
        for i in nums :
            if i in nums_set:
                return True
            nums_set.add(i)
                
        return False

        
        