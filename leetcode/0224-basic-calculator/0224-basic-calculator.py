class Solution(object):
    def calculate(self, s):

        # approached by case 3 

        stack = []

        sign = 1
        num = 0
        res = 0


        for ch in s :

            if ch == "(":
                stack.append(res) #reason to append res first to avoid cases like -(-3).first sign will multipli aft pop()
                stack.append(sign)
                res = 0
                num = 0
                sign = 1 # may be it previously -1 so to not affect res we assign 1 to sign
            
            elif ch == "-":
                res += num * sign   # add previous num with his sign to res 
                sign = -1                
                num = 0
            
            elif ch == "+":
                res += num * sign # add previous num with his sign to res
                sign = 1
                num = 0
            
            elif ch == ")":

                res += num * sign
                res = res * stack.pop() 
                res = res + stack.pop()
                num = 0
            
            elif ch.isdigit() :
                num = num * 10 + int(ch) # build multi digit number
        
        res += num * sign # after iteration may be num has value

        return res

        