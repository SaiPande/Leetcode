class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}
        lst = []
        for i in arr:
            dict1[i] = dict1.get(i,0)+1

        lst.extend(val for val in dict1.values())
        set1 = set(lst)
        if len(lst) == len(set1):
            return True
        return False