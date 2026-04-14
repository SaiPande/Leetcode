class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict1 = {}
        lst = []
        for i in arr:
            dict1[i] = dict1.get(i, 0)+1

        for key, value in dict1.items():
            if key == value:
                lst.append(key)
        
        if len(lst) != 0:
            return max(lst)        
        return -1            