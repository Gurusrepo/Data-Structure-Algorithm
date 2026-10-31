class Solution(object):
    def mySqrt(self, x):
        if x <= 0 :
            return 0
        
        elif x == 1 :
            return 1

        left = 1
        right = x 

        while left < right :
            mid = left + (right-left)//2

            if x//mid < mid :
                right = mid
            else :
                left = mid + 1
        
        return left -1
        
        