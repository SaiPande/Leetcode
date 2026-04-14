import re
class Solution:
    def isValid(self, word: str) -> bool:
        
        if (len(word)<3):
            return False
        elif not re.fullmatch(r"^[a-zA-Z0-9]+", word) :
            return False
        elif not re.search(r"[aeiouAEIOU]+", word):
            return False
        elif not re.search(r"[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]", word):
            return False
        else:
            return True    