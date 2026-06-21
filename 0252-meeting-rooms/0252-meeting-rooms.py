class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0 or  len(intervals) == 1:
            return True
        else:
            intervals.sort(key=lambda x: x[1]) 
            print(intervals)
            prev = intervals[0] 
            for i in range(1,len(intervals)):
                if intervals[i][0]<prev[1]:
                    return False
                else:
                    prev = intervals[i]    
            return True        
