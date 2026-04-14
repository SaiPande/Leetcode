class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict1 = {}
        for i in arr:
            dict1[i] = dict1.get(i, 0)+1
        lst = []
        for key, values in dict1.items():
            if values == 1:
                lst.append(key)       
        if len(lst) < k:
            return ''
        else:
            return lst[k-1]    
