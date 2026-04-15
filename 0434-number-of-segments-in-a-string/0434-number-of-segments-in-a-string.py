import re
class Solution:
    def countSegments(self, s: str) -> int:
        
        '''if s == '':
            return 0
        elif s.find('r^[a-zA-Z0-9]+'):
            return s.count(' ')+1
        else: 
            return 0    '''

        
        return  len(s.split())   