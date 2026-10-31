class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        count = 0
        end = - float('inf')
        
        intervals.sort(key = lambda X : X[1])

        for interval in intervals :
            if interval[0] >= end :
                end = interval[1]
            else :
                count += 1

        return count