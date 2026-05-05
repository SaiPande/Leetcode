class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        done = [0]*len(baskets)
        for i in range(len(fruits)):
            check = False
            for j in range(len(baskets)):
                if done[j] == 0 and fruits[i] <= baskets[j]:
                    check = True
                    done[j] = 1
                    #count += baskets[j]-fruits[i]
                    break
            if not check:
                count += 1        
        return count