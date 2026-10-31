class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0]) 
        
        left = 0
        right = (row * col)  -1 

        while left <= right :

            mid = left + (right-left)//2 
            curr = matrix[mid//col][mid%col]

            if curr == target :
                return True 
            
            if curr < target :
                left = mid + 1 
            
            else :
                right = mid -1
        
        return False
 
        