class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i,0)+1

        h= []

        for nums in dict1.keys():
            heapq.heappush(h, (dict1[nums],nums))
            if len(h)>k:
                heapq.heappop(h)        
        finalresult = []        
        for i in range(k):
            finalresult.append(heapq.heappop(h)[1])
        return finalresult  