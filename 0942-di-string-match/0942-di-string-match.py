class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        sum1 = int((high*(high+1))/2)
        lst = []
        for i in s:
            if i == 'I':
                lst.append(low)
                low += 1
            else:
                lst.append(high)
                high -= 1    
        lst.append(sum1 - sum(lst))
        return lst        