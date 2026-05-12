class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i,0)+1
        print(dict1)
        count = 0
        seen = set()
        for key,value in dict1.items():
            if (k-key) in dict1 and (k-key) not in seen:
                if key == (k-key):
                    count += (min(value, dict1[k-key]))//2
                    seen.add(key)
                else:    
                    count += min(value, dict1[k-key])
                    seen.add(key)
                    seen.add(k-key)
        return count        
