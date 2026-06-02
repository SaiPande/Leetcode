class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        minLand, minWater, result = 9999, 9999, 9999
        l = len(landStartTime)
        w = len(waterStartTime)

        for i in range(l):
            minLand = min(minLand, landStartTime[i]+landDuration[i])

        for i in range(w):
            minWater = min(minWater, waterStartTime[i]+waterDuration[i]) 
            result = min(result, max(minLand,waterStartTime[i])+ waterDuration[i]) #consider that first land ride is done and then water ride

        for i in range(l):
            result = min(result, max(minWater,landStartTime[i])+ landDuration[i])   # now check again with the results if there is any occurance where considering water ride first and then land ride gives lesser end time
        return result


