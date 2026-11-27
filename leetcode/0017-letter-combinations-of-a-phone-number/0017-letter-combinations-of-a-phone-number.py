class Solution(object):
    def letterCombinations(self, digits):

        arr = []
        map_str = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]  # consider digits each num as index you get to know why 
 
        self.generate("", arr, map_str, digits) 

        return arr
        
    def generate(self, curr, arr, map_str, digits) :

        if len(curr) == len(digits):
            arr.append(curr)
            return 
        
        i = len(curr) 

        for each in map_str[int(digits[i])] :

            self.generate(curr+each, arr, map_str, digits)


