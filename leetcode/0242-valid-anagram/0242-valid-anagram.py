class Solution(object):
    def isAnagram(self, s, t):

        # new_s = list(s)
        # new_t = list(t)
        # new_s.sort()
        # new_t.sort()

       

        # if len(new_s) != len(new_t):
        #     return False 

        # else :
        #     for i in range(len(new_s)):
        #         if new_s[i] != new_t[i] :
        #             return False 

        # return True 
        if len(s) != len(t) : return False

        uniChar = [0] * 128 

        for i in s :
            uniChar[ord(i)] += 1 
        
        for i in t :
            uniChar[ord(i)] -= 1
        
        for each in uniChar :
            if each > 0  :
                return False 
        return True
        

                            
                    
                    


        
        