class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        mx = max(nums)
        if len(nums)!=mx+1:
            return False
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i,0)+1
        for key, value in dict1.items():
            if key < mx and value != 1:
                return False    
            elif key == mx and value != 2:
                return False
        return True               