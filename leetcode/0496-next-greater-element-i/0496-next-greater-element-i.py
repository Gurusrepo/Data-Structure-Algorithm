class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        for i in range(len(nums1)) :
            index = nums2.index(nums1[i])
            for j in range(index,len(nums2)):
                if nums2[j] > nums1[i] :
                    nums1[i] = nums2[j]
                    break
            if nums1[i] == nums2[index] :
                nums1[i] = -1
        
        print(nums1)
        return nums1


        
        