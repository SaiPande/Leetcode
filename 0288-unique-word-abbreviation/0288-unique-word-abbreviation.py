class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.seen = set()
        self.dictionary = dictionary 
        self.conflicts = set() 
        for i,word in enumerate(dictionary):
            abbr = word if len(word) <= 2 else word[0]+str(len(word)-2)+word[-1]
            if abbr in self.seen and word not in self.dictionary[:i]:
                self.conflicts.add(abbr)
                self.seen.remove(abbr)
            else:
                self.seen.add(abbr)

    def isUnique(self, word: str) -> bool:
        abbr = word if len(word) <= 2 else word[0]+str(len(word)-2)+word[-1]
        if abbr in self.conflicts:
            return False
            
        if len(word) <= 2 and word in self.seen and word not in self.dictionary:
            return False        
        else:
            if abbr in self.seen and word not in self.dictionary:
                return False
            else:
                return True                    


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)