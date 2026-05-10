class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = ''.join(chunks)
        dict1 = {}
        cleanlst = ''
        for i in range(len(s)):
            if s[i] >= 'a' and s[i]<='z':
                cleanlst+=(s[i])
            elif s[i] == '-':
                if i!=0 and i<(len(s)-1) and s[i-1]>='a' and s[i-1]<='z' and s[i+1]>='a' and s[i+1]<='z':
                    cleanlst+=(s[i])
                else:
                    cleanlst+=(' ')
            else:
                cleanlst+=(' ')
        
        lst = cleanlst.split()
        
        for i in lst:
            dict1[i] = dict1.get(i,0)+1   
        opt = []
        for i in range(len(queries)):
            if queries[i] in dict1:
                opt.append(dict1[queries[i]])
            else:
                opt.append(0)       
        return opt        