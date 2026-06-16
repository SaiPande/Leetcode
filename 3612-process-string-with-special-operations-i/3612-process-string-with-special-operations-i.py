class Solution:
    def processStr(self, s: str) -> str:
        i = 0
        t = []
        sarray = list(s)
        while i<len(sarray):
            if sarray[i] == '*':
                if len(t)!=0:
                    t.pop()
            elif sarray[i] == '#':
                t.extend(t)
            elif sarray[i] == '%':
                t.reverse()
            else:
                t.append(sarray[i])
            i+=1
        st = ''.join(t)
        return st
