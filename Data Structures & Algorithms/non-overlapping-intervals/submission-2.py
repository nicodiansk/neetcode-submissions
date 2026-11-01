class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i: i[0])
        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd:
                res+=1
                lastEnd = min(end, lastEnd)
            else:
                lastEnd = end
        return res
