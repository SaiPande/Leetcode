class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        outputlist = []
        for i in nums1:
            if i in nums2:
                index = nums2.index(i)
                max = -1
                flag = False
                for j in nums2[index:]:
                    if j > i:
                        outputlist.append(j)
                        flag = True
                        break
                if flag == False:
                    outputlist.append(-1)     

        return outputlist                
