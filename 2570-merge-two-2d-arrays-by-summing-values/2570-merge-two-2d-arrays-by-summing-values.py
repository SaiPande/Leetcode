class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.extend(nums2)
        dict = {}
        for i in nums1:
            if i[0] in dict:
                dict[i[0]] += i[1]
            else:    
                dict[i[0]] = i[1] 
        result = [[key, value] for key,value in dict.items()]
        result.sort(key = lambda x:x[0])
        return result
                  


