class Solution(object):
    def compress(self, chars):
        count = 0 
        index = 0 

        for i in range(len(chars)):
            count += 1 

            if i+1 == len(chars) or chars[i] != chars[i+1] :
                chars[index] = chars[i] 
                index += 1 
                if count > 1 :
                    for eachDigit in str(count):
                        chars[index] = eachDigit
                        index += 1 
                count = 0 
                
        return index














        # count = 0
        # index = 0 

        # for i in range(len(chars)):
        #     count += 1
        #     if (i+1 == len(chars)) or chars[i] != chars[i+1] :
        #         chars[index] = chars[i]
        #         index += 1

        #         if count > 1 :
        #             for ch in str(count):
        #                 chars[index] = ch 
        #                 index += 1 
                
        #         count = 0 
        
        return index


        