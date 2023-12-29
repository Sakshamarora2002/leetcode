class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        test=True
        for i in range (len(intervals)):
            if intervals[i][0]>newInterval[0]:
                test=False
                intervals.insert(i,newInterval)
        if test:
            intervals.append(newInterval)
        i=1
        while i<len(intervals):
            if intervals[i-1][1]>=intervals[i][0]:
                intervals[i-1][1]=max (intervals[i-1][1],intervals[i][1])
                intervals.pop(i)
            else:
                i=i+1
        return intervals

     