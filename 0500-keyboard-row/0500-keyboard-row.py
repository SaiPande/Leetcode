class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u','i', 'o','p'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        flags = []
        for i in words:
            flag = 0
            lowerstr = i.lower()
            if lowerstr[0] in set1:
                for j in lowerstr:
                    if j not in set1: 
                        flag = 1 
                        break
            elif lowerstr[0] in set2:
                for j in lowerstr:
                    if j not in set2: 
                        flag = 1 
                        break
            elif lowerstr[0] in set3:
                for j in lowerstr:
                    if j not in set3: 
                        flag = 1 
                        break
            if flag == 0:
                flags.append(i)        

        '''if len(flags) != 0:
            return flags
        else:
            return []
        '''
        return flags        
