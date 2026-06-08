class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        words = title.split(' ')
        capstr = ''

        for word in words:
            if len(word)<= 2:
                capstr = capstr+" "+word.lower()
            else:
                capstr = capstr+" "+word.capitalize()    
        return capstr.strip()        