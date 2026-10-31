class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        # arr = list(magazine)
        # for i in ransomNote :
        #     if i in arr :
        #         arr.remove(i)
                 
        #     else :
        #         return False
        # return True

        asci = [0] * 128 

        for i in magazine :
            asci[ord(i)] += 1 
        
        for i in ransomNote :
             asci[ord(i)] -= 1 
        
        for i in ransomNote:
            if asci[ord(i)] < 0 :
                return False

        
        return True

        