class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        nonoverlaplist = []
        nonoverlaplist.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= nonoverlaplist[-1][1]:
                nonoverlaplist[-1][1] = max(nonoverlaplist[-1][1], intervals[i][1])   
            else:
                nonoverlaplist.append(intervals[i])   
        return nonoverlaplist        

        # for i in range(1,len(intervals)):
        #     if intervals[i-1][1] >= intervals[i][0]:
        #         if nonoverlaplist and intervals[i-1] == nonoverlaplist[-1]:
        #             nonoverlaplist.pop()
        #         if intervals[i][1]>intervals[i-1][1]:
        #             nonoverlaplist.append([intervals[i-1][0],intervals[i][1]])
        #         else:
        #             nonoverlaplist.append(intervals[i-1])    
        #     else:
        #         nonoverlaplist.append(intervals[i])            

        # return nonoverlaplist
