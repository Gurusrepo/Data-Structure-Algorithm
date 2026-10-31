class Solution(object):
    def targetIndices(self, nums, target):
        index_arr = []
        nums.sort()

        for i  in range(len(nums)) :
            if nums[i] == target:
                index_arr.append(i)
        
        return index_arr


