class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        lst1 = dict(zip(list('abcdefghijklmnopqrstuvwxyz'),widths))

        count = 0
        line = 1
        remaining = 0
        for i in s:
            if count + lst1[i] > 100:
                line += 1
                count = lst1[i]
            else:
                count += lst1[i]   
       
        remaining = count
        return [line, remaining]                