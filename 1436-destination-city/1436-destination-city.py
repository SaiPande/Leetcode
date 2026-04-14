class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citi = []
        
        lst = list((path[1] for path in paths))
        #print(lst)

        for i in range(0,len(paths)):
            print(paths[i][0])
            if paths[i][0] in lst:
                citi.append(paths[i][0])

        for i in lst:
            if i not in citi:
                return i

        return ''        