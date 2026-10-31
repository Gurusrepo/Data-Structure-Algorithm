class Solution(object):
    def insert(self, intervals, newInterval):
        new_arr = []

        for interval in intervals:

            if interval[1] < newInterval[0]:
                new_arr.append(interval)
            
            elif interval[0] > newInterval[1] :
                new_arr.append(interval)
                 
            else :
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1]) 
            
        new_arr.append(newInterval)
        new_arr.sort()

        return new_arr
         