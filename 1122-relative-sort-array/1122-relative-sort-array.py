class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1 = {}
        lst = []
        lst2 = []

        for i in arr1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in arr2:
            if i in dict1:
                lst.extend([i]*dict1[i])

        for i in arr1:
            if i not in lst:
                lst2.append(i)

        lst2.sort()
        lst.extend(lst2)                  

        return lst